#Criado em 27 de Maio de 2023 - Versão 1.0
#Julio Antonio do Amaral 
#julio.amaral@foursys.com.br 

def html_to_react(html: str) -> str:
    react_code = html.replace('<div>', '<div>').replace('</div>', '</div>')
    return react_code

if __name__ == "__main__":
    html_code = "<div>Hello World!</div>"
    react_code = html_to_react(html_code)
    print(react_code)

