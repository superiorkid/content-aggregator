<!--
Hey, thanks for using the awesome-readme-template template.
If you have any enhancements, then fork this project and create a pull request
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->
<div align="center">

  <img src="app/static/img/Pajarito-Pirate.svg" alt="logo" width="200" height="auto" />
  <h1>DemoGregator</h1>
  
  <p>
    Simple content aggregator website using flask
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://github.com/superiorkid/content-aggregator/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/superiorkid/content-aggregator" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/superiorkid/content-aggregator" alt="last update" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/network/members">
    <img src="https://img.shields.io/github/forks/superiorkid/content-aggregator" alt="forks" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/stargazers">
    <img src="https://img.shields.io/github/stars/superiorkid/content-aggregator" alt="stars" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/issues/">
    <img src="https://img.shields.io/github/issues/superiorkid/content-aggregator" alt="open issues" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/superiorkid/content-aggregator.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://demogregator.herokuapp.com/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/superiorkid/content-aggregator/issues/">Report Bug</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  - [Prerequisites](#bangbang-prerequisites)
  - [Installation](#gear-installation)
  - [Run Locally](#running-run-locally)
  <!-- About the Project -->

## :star2: About the Project

<!-- Screenshots -->

### :camera: Screenshots

<div align="center"> 
  <img src="app/static/img/demo.png" alt="screenshot" />
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://flask.palletsprojects.com/">Flask</a></li>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
    <li><a href="https://www.postgresql.org/">Postgresql</a></li>
  </ul>

<!-- Features -->

### :dart: Features

- User Register/Login
- Bookmark Articles
- Read Articles
- Admin

<!-- Env Variables -->

### :key: Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GITHUB_OAUTH_CLIENT_ID` <br>
`GITHUB_OAUTH_CLIENT_SECRET` <br>
`GOOGLE_OAUTH_CLIENT_ID` <br>
`GOOGLE_OAUTH_CLIENT_SECRET` <br>
`MAIL_USERNAME` <br>
`MAIL_PASSWORD` <br>
`IS_ADMIN`

<!-- Getting Started -->

## :toolbox: Getting Started

<!-- Run Locally -->

### :running: Run Locally

Clone the project

```bash
  git clone https://github.com/superiorkid/content-aggregator.git
```

Go to the project directory

```bash
  cd content-aggregator
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```
