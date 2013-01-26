<!DOCTYPE html>
<!-- 
  Design by predic8 GmbH
  http://www.predic8.de
  Released for free under a Creative Commons Attribution 2.5 License
-->
<html>
  <head>
    <meta name="viewport" content="user-scalable=no, width=device-width"/>
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <link rel="stylesheet" type="text/css" href="/static/iphone.css" media="screen"/>
  </head>
  <body>
    <div>
      <div class="button"><a href="/">Back</a></div>
      <h1>{{ device['name'] }}</h1>
      <h2 class="temp">{{ device['temp'] }}</h2>
      <ul>
          <li>Name: <span class="right">{{ device['name'] }}</span></li>
          <li>Updated: <span class="right">{{ device['time'] }}</span></li>
      </ul>
      <p>TempMon 0.1</p>
    </div>
  </body>
</html>
         