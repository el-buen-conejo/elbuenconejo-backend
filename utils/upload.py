import cloudinary.uploader


def upload_image_to_cloudinary(image, target):
    upload_result = cloudinary.uploader.upload(image, folder=target)
    return upload_result["url"]
