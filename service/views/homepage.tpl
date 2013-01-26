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
      <ul>
        %for device in devices:
          <li>{{ device['name'] }}<span class="right">{{ device['temp'] }}</span></li>
        %end
      </ul>
      <p>TempMon 0.1</p>
    </div>
  </body>
</html>
         