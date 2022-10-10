from countryinfo import CountryInfo
from flask import Flask, request, render_template
from form import myForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b04eb14ce09be750f1d5db107c255932'


# print(f"{}'s alternative spelling is : ", country.alt_spellings())
# print(f"The capital of {}' is : ", country.capital())


@app.route('/', methods=['GET', 'POST'])
def index():
    form = myForm()
    try:
        if request.method == 'POST':
            country_ = form.country_name.data
            country_ = country_.title()
            country = CountryInfo(country_)
            return render_template('index.html', country_=country_, form=form, country=country)
    except Exception as e:
        error = 'No Info available for this country'
        return render_template('index.html', form=form, error=error, e=e)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
