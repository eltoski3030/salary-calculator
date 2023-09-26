from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

class Employee:
    def __init__(self, first, last, pay, job_exp):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.job_exp = job_exp

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def salary_calculator(self):
        if self.job_exp >= 3:
            average_salary = 4.5 * self.pay
        else:
            average_salary = self.pay
        return average_salary

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        salary = float(request.form["salary"])
        job_experience = int(request.form["job_experience"])

        employee = Employee(first_name, last_name, salary, job_experience)
        estimated_salary = employee.salary_calculator()
        
        return render_template("result.html", 
                               fullname=employee.fullname(), 
                               email=employee.email, 
                               salary=employee.pay, 
                               estimated_salary=estimated_salary)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
