from flask import Flask 
app = Flask(__name__) 
 
@app.route("/") 
def home(): 
    return """ 
    <h1>¡Hola! Soy Carlos</h1> 
    <p>Estudio en: UVM</p> 
    <p>Me gusta: Salir con amigos y familia</p> 
    <p><em>"Si no te averguenzas un poco de lo que hiciste el año pasado, entonces no aprendiste lo suficiente"</em></p> 
    """ 

if __name__ == "__main__":
    app.run()
