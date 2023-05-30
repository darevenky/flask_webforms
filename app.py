from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
FI=Flask(__name__)


class NameForm(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()


@FI.route('/webform',methods=['POST','GET'])
def webform():
    FO=NameForm()

    if request.method=='POST':
        fd=NameForm(request.form)
        if fd.validate():
            return fd.name.data
    return render_template('webform.html',FO=FO)


if __name__=='__main__':
    FI.run(debug=True)