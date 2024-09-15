import logging
import time
from logging.handlers import SysLogHandler

import boto3


def configure_cloudwatch_logger():
    # Configurar el cliente de CloudWatch
    cloudwatch = boto3.client(
        "logs", region_name="us-east-1"
    )  # Cambia 'us-east-1' por tu región

    # Configurar el logger de Gunicorn
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Configurar el handler de syslog para enviar logs a CloudWatch
    handler = SysLogHandler(address="/dev/log")
    formatter = logging.Formatter("%(asctime)s %(message)s", datefmt="%b %d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Definir la función para enviar logs a CloudWatch
    def send_logs_to_cloudwatch(log_data):
        log_group_name = "your-log-group-name"
        log_stream_name = f'{log_group_name}-{time.strftime("%Y-%m-%d-%H-%M-%S")}'

        # Create the log stream if it doesn't exist
        try:
            cloudwatch.describe_log_streams(
                logGroupName=log_group_name, logStreamNamePrefix=log_stream_name
            )
        except cloudwatch.exceptions.ResourceNotFoundException:
            cloudwatch.create_log_stream(
                logGroupName=log_group_name, logStreamName=log_stream_name
            )

        # Send log data to CloudWatch
        log_events = [{"timestamp": int(time.time() * 1000), "message": log_data}]
        cloudwatch.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=log_events,
        )

    # Enviar logs al handler de syslog
    def application(environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            log_data = '%s - - [%s] "%s %s" %s' % (
                environ.get("REMOTE_ADDR"),
                time.strftime("%d/%b/%Y %H:%M:%S"),
                environ.get("REQUEST_METHOD"),
                environ.get("PATH_INFO"),
                status,
            )
            send_logs_to_cloudwatch(log_data)
            return start_response(status, headers, exc_info)

        return application(environ, custom_start_response)
