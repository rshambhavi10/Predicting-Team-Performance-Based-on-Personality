import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model12.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
   
	g=0
	ei=0
	si=0
	tf=0
	jp=0

	size=int(request.form.get("team_size"))

	
	if(size==4):


		g1=request.form.get("gender1")
		ei1=request.form.get("ei1")
		si1=request.form.get("si1")
		tf1=request.form.get("tf1")
		jp1=request.form.get("jp1")
		coop1=int(request.form.get("coop1"))
		free1=int(request.form.get("free1"))
		app1=int(request.form.get("app1"))
		equal1=int(request.form.get("equal1"))

		g2=request.form.get("gender2")
		ei2=request.form.get("ei2")
		si2=request.form.get("si2")
		tf2=request.form.get("tf2")
		jp2=request.form.get("jp2")
		coop2=int(request.form.get("coop2"))
		free2=int(request.form.get("free2"))
		app2=int(request.form.get("app2"))
		equal2=int(request.form.get("equal2"))

		g3=request.form.get("gender3")
		ei3=request.form.get("ei3")
		si3=request.form.get("si3")
		tf3=request.form.get("tf3")
		jp3=request.form.get("jp3")
		coop3=int(request.form.get("coop3"))
		free3=int(request.form.get("free3"))
		app3=int(request.form.get("app3"))
		equal3=int(request.form.get("equal3"))

		g4=request.form.get("gender4")
		ei4=request.form.get("ei4")
		si4=request.form.get("si4")
		tf4=request.form.get("tf4")
		jp4=request.form.get("jp4")
		coop4=int(request.form.get("coop4"))
		free4=int(request.form.get("free4"))
		app4=int(request.form.get("app4"))
		equal4=int(request.form.get("equal4"))

		if (g1=="Female"):
			g+=1

		if (g2=="Female"):
			g+=1

		if (g3=="Female"):
			g+=1

		if (g4=="Female"):
			g+=1


		if (ei1=="Introvert"):
			ei+=1

		if (ei2=="Introvert"):
			ei+=1

		if (ei3=="Introvert"):
			ei+=1

		if (ei4=="Introvert"):
			ei+=1


		if (si1=="Intuition"):
			si+=1

		if (si2=="Intuition"):
			si+=1

		if (si3=="Intuition"):
			si+=1

		if (si4=="Intuition"):
			si+=1


		if (tf1=="Thinking"):
			tf+=1

		if (tf2=="Thinking"):
			tf+=1

		if (tf3=="Thinking"):
			tf+=1

		if (tf4=="Thinking"):
			tf+=1


		if (jp1=="Judging"):
			jp+=1

		if (jp2=="Judging"):
			jp+=1

		if (jp3=="Judging"):
			jp+=1

		if (jp4=="Judging"):
			jp+=1

		coop=(coop1+coop2+coop3+coop4)/4
		free=(free1+free2+free3+free4)/4
		app=(app1+app2+app3+app4)/4
		equal=(equal1+equal2+equal3+equal4)/4

	else:

		g1=request.form.get("gender1")
		ei1=request.form.get("ei1")
		si1=request.form.get("si1")
		tf1=request.form.get("tf1")
		jp1=request.form.get("jp1")
		coop1=request.form.get("coop1")
		free1=request.form.get("free1")
		app1=request.form.get("app1")
		equal1=request.form.get("equal1")

		g2=request.form.get("gender2")
		ei2=request.form.get("ei2")
		si2=request.form.get("si2")
		tf2=request.form.get("tf2")
		jp2=request.form.get("jp2")
		coop2=request.form.get("coop2")
		free2=request.form.get("free2")
		app2=request.form.get("app2")
		equal2=request.form.get("equal2")

		g3=request.form.get("gender3")
		ei3=request.form.get("ei3")
		si3=request.form.get("si3")
		tf3=request.form.get("tf3")
		jp3=request.form.get("jp3")
		coop3=request.form.get("coop3")
		free3=request.form.get("free3")
		app3=request.form.get("app3")
		equal3=request.form.get("equal3")

		if (g1=="Female"):
			g+=1

		if (g2=="Female"):
			g+=1

		if (g3=="Female"):
			g+=1

		


		if (ei1=="Introvert"):
			ei+=1

		if (ei2=="Introvert"):
			ei+=1

		if (ei3=="Introvert"):
			ei+=1

		


		if (si1=="Intuition"):
			si+=1

		if (si2=="Intuition"):
			si+=1

		if (si3=="Intuition"):
			si+=1

		


		if (tf1=="Thinking"):
			tf+=1

		if (tf2=="Thinking"):
			tf+=1

		if (tf3=="Thinking"):
			tf+=1

		


		if (jp1=="Judging"):
			jp+=1

		if (jp2=="Judging"):
			jp+=1

		if (jp3=="Judging"):
			jp+=1

		

		coop=(coop1+coop2+coop3)/3
		free=(free1+free2+free3)/3
		app=(app1+app2+app3)/3
		equal=(equal1+equal2+equal3)/3


	




	team_size=size


	fp=g/team_size
	if(fp>=0.5):
		femalePercent=1
	else:
		
		femalePercent=0



	eip=ei/team_size
	if(eip>=0.5):
		introvertPercent=1
	else:
		
		introvertPercent=0


	sip=si/team_size
	if(sip>=0.5):
		intuitionPercent=1
	else:
		
		intuitionPercent=0


	tfp=tf/team_size
	if(tfp>=0.5):
		thinkingPercent=1
	else:
		
		thinkingPercent=0


	jpp=jp/team_size
	if(jpp>=0.5):
		judgingPercent=1
	else:
		
		judgingPercent=0

	
	if (coop>=0.5):
		cooperation=1
	else:
		cooperation=0

	if (free>=0.5):
		freedom=1
	else:
		freedom=0

	if (app>=0.5):
		appreciate=1
	else:
		appreciate=0

	if (equal>=0.5):
		equal_cont=1
	else:
		equal_cont=0


	#int_features = [int(x) for x in request.form.values()]
	l=[team_size, femalePercent, introvertPercent, intuitionPercent, thinkingPercent, judgingPercent, cooperation, freedom, appreciate, equal_cont]
	int_features = [int(x) for x in l]

	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	output = prediction[0]
	return render_template('index.html', prediction_text='The team is effective? {}'.format(output))
'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
    
'''
'''
    For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
'''
if __name__ == "__main__":
	app.run(debug=True)
