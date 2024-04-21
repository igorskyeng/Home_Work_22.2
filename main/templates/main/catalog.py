from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Skystore</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
<div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow">
    <h5 class="my-0 mr-md-auto font-weight-normal">Skystore</h5>
    <nav class="ms-5">
        <a class="p-2 btn btn-outline-primary" href="/">Каталог</a>
        <a class="p-2 btn btn-outline-primary" href="/contacts/">Контакты</a>
    </nav>
</div>

<div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
    <h1 class="display-4">Контакты</h1>
</div>

<div class="container">
    <div class="row text-start">
        <div class="col-lg-9 col-md-6 col-sm-12">
            <div class="card mb-4 box-shadow">
                <div class="card-body">
                    <table class="table table-striped">
                        <tr>
                            <td class="w-25">Страна</td>
                            <td>USA</td>
                        </tr>
                        <tr>
                            <td class="w-25">ИНН</td>
                            <td>91-1144442</td>
                        </tr>
                        <tr>
                            <td class="w-25">Адрес</td>
                            <td>Redmond,WA,98052-6399</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-12">
            <div class="card mb-4 box-shadow">
                <div class="card-header">
                    <h4 class="my-0 font-weight-normal">Свяжитесь с нами</h4>
                </div>
                <div class="card-body">
                    <form method="post" action="" class="form-floating">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name">Имя</label>
                            <input type="text" name="name" class="form-control" id="name" placeholder="Ваше имя" required>
                        </div>
                        <div class="mb-3">
                            <label for="phone">Телефон</label>
                            <input type="text" name="phone" class="form-control" id="phone" placeholder="Контактный телефон" required>
                        </div>
                        <div class="mb-3">
                            <label for="message">Сообщение</label>
                            <textarea type="text" name="message" class="form-control" id="message" placeholder="Контактный телефон" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-lg btn-block btn-outline-primary">Отправить</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <footer class="pt-4 my-md-5 pt-md-5 border-top">
        <div class="row">
            <div class="col-12 col-md">
                SkyStore
                <small class="d-block mb-3 text-muted">&copy; 2023</small>
            </div>
            <div class="col-6 col-md">
                <h5>Категории</h5>
                <ul class="list-unstyled text-small">
                    <li><a class="text-muted" href="#">Рассылки</a></li>
                    <li><a class="text-muted" href="#">Телеграм боты</a></li>
                    <li><a class="text-muted" href="#">Полезные утилиты</a></li>
                    <li><a class="text-muted" href="#">Веб-приложения</a></li>
                    <li><a class="text-muted" href="#">Микросервисы</a></li>
                </ul>
            </div>
            <div class="col-6 col-md">
                <h5>Дополнительно</h5>
                <ul class="list-unstyled text-small">
                    <li><a class="text-muted" href="#">Мы пишем</a></li>
                </ul>
            </div>
            <div class="col-6 col-md">
                <h5>О нас</h5>
                <ul class="list-unstyled text-small">
                    <li><a class="text-muted" href="/contacts/">Контакты</a></li>
                </ul>
            </div>
        </div>
    </footer>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</body>
</html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
