from flask import Flask, render_template, request

app = Flask(__name__)

#ЦДА
@app.route('/', methods=['GET', 'POST'])
def algorithm_1():
    return render_template('algorithm_1.html')


#Брезенхем
@app.route('/algorithm_2')
def algorithm_2():
    return render_template('algorithm_2.html')

#Ву
@app.route('/algorithm_3')
def algorithm_3():
    return render_template('algorithm_3.html')


@app.route('/circle', methods=['GET', 'POST'])
def circle():
    return render_template('circle.html')

@app.route('/ellipse')
def ellipse():
    return render_template('ellipse.html')

@app.route('/parabola')
def parabola():
    return render_template('parabola.html')

@app.route('/hyperbola', methods=['GET', 'POST'])
def hyperbola():
    return render_template('hyperbola.html')

@app.route('/hermite', methods=['GET', 'POST'])
def hermite():
    return render_template('hermite.html')

@app.route('/bezier', methods=['GET', 'POST'])
def bezier():
    return render_template('bezier.html')

@app.route('/b_spline', methods=['GET', 'POST'])
def b_spline():
    return render_template('b_spline.html')

@app.route('/objects_3d', methods=['GET', 'POST'])
def objects_3d():
    return render_template('objects_3d.html')
    
@app.route('/polygon_graham', methods=['GET', 'POST'])
def polygon_graham():
    return render_template('polygon_graham.html')

@app.route('/polygon_jarvis', methods=['GET', 'POST'])
def polygon_jarvis():
    return render_template('polygon_jarvis.html')

@app.route('/polygon_connection', methods=['GET', 'POST'])
def polygon_connection():
    return render_template('polygon_connection.html')

@app.route('/polygon_filling_algorithm_1', methods=['GET', 'POST'])
def polygon_filling_algorithm_1():
    return render_template('polygon_filling_algorithm_1.html')

@app.route('/polygon_filling_algorithm_2', methods=['GET', 'POST'])
def polygon_filling_algorithm_2():
    return render_template('polygon_filling_algorithm_2.html')

@app.route('/polygon_filling_algorithm_3', methods=['GET', 'POST'])
def polygon_filling_algorithm_3():
    return render_template('polygon_filling_algorithm_3.html')

@app.route('/polygon_filling_algorithm_4', methods=['GET', 'POST'])
def polygon_filling_algorithm_4():
    return render_template('polygon_filling_algorithm_4.html')

@app.route('/polygon_delaunay', methods=['GET', 'POST'])
def polygon_delaunay():
    return render_template('polygon_delaunay.html')

@app.route('/polygon_voronoi', methods=['GET', 'POST'])
def polygon_voronoi():
    return render_template('polygon_voronoi.html')

from waitress import serve
if __name__ == "__main__":
    serve(app, port=8080)
    #app.run(debug=True, port=8080)