<!doctype html>
<!-- default.tpl -->
<HTML lang="en">
  <HEAD>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <TITLE>{{ title }}</TITLE>
  </HEAD>
  <body>
    <div id="menu">
      <nav>
        <ul>
            <li><a href="/club">club</a></li>
            <li><a href="/contact">contact</a></li>
            <li><a href="/media">media</a></li>
            <li><a href="/news">news</a></li>
            <li><a href="/teams">teams</a></li>
        </ul>
      </nav>
    </div>
    
    <div id="content">
      {{ !base }}
    </div>
  </body>
  <footer>
    <p></p>
  </footer>
</html>