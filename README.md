<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/el-buen-conejo/elbuenconejo-backend">
    <img src="https://github.com/el-buen-conejo/elbuenconejo-backend/blob/961be498851fc7b1e9d940550e7eb54ea3b2130f/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">API El Buen Conejo</h3>

  <p align="center">
    A manager for playlist's streaming videos in local mode!
    <br />
    <a href="https://github.com/el-buen-conejo/elbuenconejo-backend"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://service-streaming.onrender.com/">View Demo</a>
    ·
    <a href="https://github.com/el-buen-conejo/elbuenconejo-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/el-buen-conejo/elbuenconejo-backend/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/el-buen-conejo/elbuenconejo-backend/blob/82a8c694a418723faacf992c5dd76b6e328120f8/api_playlists.png)

It is a project to congregate rabbit farmers, trading rabbits, meat, and other derivate products, and finally share statistics with the community, industry, and government.

In this project the objetives are:
* Create a local database with PostgreSQL through Django ORM
* Use JWT with custom user model
* Login with username, email and password
* Send email for activate users
* Create the REST API for CRUD operations through Django Rest Framework
* Use Swagger for document the REST API
* Upload photos for profiles, cages, farms and rabbbits in Cloudinary service
* Use docker containers and docker compose


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With



[![Python][Python]][Python-url]
[![Django][Django]][Django-url]
[![DjangoREST][DjangoREST]][DjangoREST-url]
[![Swagger][Swagger]][Swagger-url]
[![JWT][JWT]][JWT-url]
[![Postgres][Postgres]][Postgres-url]
[![Docker][Docker]][Docker-url]
[![Ubuntu][Ubuntu]][Ubuntu-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

This project use a postgreSQL database and docker container in local mode and production.




### Installation


1. Clone the repository
   ```sh
   git clone git@github.com:el-buen-conejo/elbuenconejo-backend.git
   ```
2. In local mode install docker and docker compose
3. Create a .env file with the environment variables of the .env.example file
4. Execute the next command with docker compose
   ```sh
   docker compose up -d 
   ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In the next link can you use the API, the indications are:
For endpoints of methods different from GET

1. Create an user with the endpoint: /api/auth/register/ of swagger ui url
2. Copy access token
3. Click in authorized button
4. Paste acces token in value field
5. Click in Authorize button
6. Click in close button
7. Can you use the API 
8. Logout in authorize button

For endpoints of methods GET only excute the endpoint in swagger ui url

_For more examples, please refer to the [Documentation](https://service-streaming.onrender.com/)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ X ] Add CI/CD with Github Actions
- [   ] Terminate swagger documentation
- [   ] Add versioning control
- [ X ] Deploy in Railway


See the [open issues](https://github.com/el-buen-conejo/elbuenconejo-backend/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Miguel Angel López Monroy - [@miguellopezmdev](https://twitter.com/miguellopezmdev) - miguel.lopezm.dev@gmail.com

Project Link: [https://service-streaming.onrender.com/](https://service-streaming.onrender.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

My favorite resources used:

* [Choose an Open Source License](https://choosealicense.com)
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Django Rest Framework Documentation](https://www.django-rest-framework.org/)
* [Django Class Based View Inspector](http://ccbv.co.uk/)
* [Classy Django Rest Framework](https://www.cdrf.co/)
* [Platzi Platform](https://platzi.com/)
* [Udemy Platform](https://www.udemy.com/)
* [Real Python Tutorials](https://realpython.com/)
* [Blog Developer.pe](http://www.developerpe.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mikelm2020/video-streaming.svg?style=for-the-badge
[contributors-url]: https://github.com/el-buen-conejo/elbuenconejo-backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mikelm2020/video-streaming.svg?style=for-the-badge
[forks-url]: https://github.com/el-buen-conejo/elbuenconejo-backend/network/members
[stars-shield]: https://img.shields.io/github/stars/mikelm2020/video-streaming.svg?style=for-the-badge
[stars-url]: https://github.com/el-buen-conejo/elbuenconejo-backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/mikelm2020/video-streaming.svg?style=for-the-badge
[issues-url]: https://github.com/el-buen-conejo/elbuenconejo-backend/issues
[license-shield]: https://img.shields.io/github/license/mikelm2020/video-streaming.svg?style=for-the-badge
[license-url]: https://github.com/el-buen-conejo/elbuenconejo-backend/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/miguellopezmdev
[product-screenshot]: https://github.com/el-buen-conejo/elbuenconejo-backend/blob/82a8c694a418723faacf992c5dd76b6e328120f8/api_playlists.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/es/4.0/topics/
[DjangoREST]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[DjangoREST-url]: https://www.django-rest-framework.org/
[Swagger]: https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white
[Swagger-url]: https://swagger.io/
[JWT]: https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens
[JWT-url]: https://jwt.io/
[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Ubuntu]: https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white
[Ubuntu-url]: https://ubuntu.com/download

