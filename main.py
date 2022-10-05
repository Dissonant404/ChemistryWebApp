from flask import Flask, redirect, url_for, render_template, request, abort,send_from_directory
import os
from random import randint
from math import gcd
from functools import reduce
from sympy import *
init_printing(use_unicode=True)
import math
import re

app = Flask(__name__, template_folder='Templates')

@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.png',mimetype='image/png')

@app.route("/")
def home():
	  
	return render_template("home.html")

@app.route("/molarcalc")
def Molar():
	return render_template("molarcalc.html")


@app.route("/molarcalc/mole")
def mole():

	return render_template("mole.html")

@app.route("/molarcalc/mole/result", methods=["POST"])
def result_mole():
	if request.method=="POST":
		# try:	
			var1 = float(request.form["var1"])
			var2 = float(request.form["var2"])
			option1 = request.form["option1"]
			option2 = request.form["option2"]
			res=0
			eqn=None
			s="Mole = "
			if (option1=="mass (g)" and option2=="Molar mass")  :
				res = float(var1) / float(var2)
				eqn = "Equation → Mole = mass / molar mass"
				# return render_template('mole.html',res=res)
			elif (option2=="mass (g)" and option1=="Molar mass"):
				res = float(var2) / float(var1)
				eqn = "Equation → Mole = mass / molar mass"

			elif (option1 == "conc (mol/dm^3)" and option2=="Volume (dm^3)") or (option2 == "conc (mol/dm^3)" and option1=="Volume (dm^3)"):
				res = float(var1)*float(var2)
				eqn = "Equation → mole = concentration (mol/dm^3) x (Volume (cm^3) /1000) "
			elif  (option1 == "conc (mol/dm^3)" and option2=="Volume (cm^3)") :
				var2 = var2/1000
				res = float(var1)* float(var2)
				eqn = "Equation → mole = concentration (mol/dm^3) x Volume (dm^3) "

			elif  (option2 == "conc (mol/dm^3)" and option1=="Volume (cm^3)"):
				var1 = var1/1000
				res = float(var1)* float(var2)
				eqn = "Equation → mole = concentration (mol/dm^3) x (Volume (cm^3) /1000)"

			

			elif (option1 == "avogadro constant (6 x 10^23)" and option2 == "number of particles"):
				res = float(var2)/float(6*10**23)
				eqn = "Equation → mole = no of particles / avogadro constant"
			elif (option2 == "avogadro constant (6 x 10^23)" and option1 == "number of particles"):

				res = float(6*10**23)/float(var2)
				eqn = "Equation → mole = no of particles / avogadro constant"

			elif (option1 == "molar volume constant(24 dm^3)" and option2 == "Volume (dm^3)"):
				res = float(var2)/float(var1)
				eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
			elif (option2 == "molar volume constant(24 dm^3)" and option1== "Volume (dm^3)"):
				res = float(var1)/float(var2)
				eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
			elif (option1 == "molar volume constant(24 dm^3)" and option2 == "Volume (dm^3)"):
				var2=var2/1000
				res = float(var2)/float(var1)
				eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
			elif (option2 == "molar volume constant(24 dm^3)" and option1== "Volume (cm^3)"):
				var1 = var1/1000
				res = float(var1)/float(var2)
				eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
			else:
				eqn = "Invalid Input"
		  
		  			
			return render_template('mole.html',res=round(res,3),s=s,eqn=eqn,mol="mol")

		# except ValueError:
	 #  		eqn = "Input something"
	 #  		return render_template('mole.html',eqn=eqn)

@app.route("/molarcalc/vol")
def vol():
	return render_template("vol.html")

@app.route("/molarcalc/vol/result", methods=["POST"])
def vol_result():  
	if request.method=="POST":
		
# element = request.form["element"]
		var1 = float(request.form["var1"])
		var2 = float(request.form["var2"])
		option1 = request.form["option1"]
		option2 = request.form["option2"]
		res=0
		eqn=None
		s="Volume = "
		if (option2=="mole" and option1=="conc (mol/dm^3)"):
			res = float(var2)/float(var1)
			eqn = "Equation → Volume = mole / concentration(mol/dm^3) "
		elif (option1=="mole" and option2=="conc (mol/dm^3)"):
			res = float(var1)/float(var2)
			eqn = "Equation → Volume = mole / concentration(mol/dm^3) "
		elif (option1=="mole" and option2 == "molar volume constant(24 dm^3)") or (option2=="mole" and option1 == "molar volume constant(24 dm^3)"):
			res = float(var1)*float(var2)
			eqn = "Equation → Volume (gas) = mol x molar volume constant(24 dm^3)"

		return render_template('vol.html',res=round(res,3),s=s,eqn=eqn,vol="dm^3")

@app.route("/molarcalc/conc")
def conc():
	return render_template("conc.html")
	
@app.route("/molarcalc/conc/result", methods=["POST"])
def conc_result():
	if request.method=="POST":
		
		var1 = float(request.form["var1"])
		var2 = float(request.form["var2"])
		option1 = request.form["option1"]
		option2 = request.form["option2"]
		res=0
		eqn=None
		s="concentration = "

		if(option2=="mole" and option1=="Volume (dm^3)"):
			res = float(var2)/float(var1)
			eqn = "Equation → concentration(mol/dm^3) = mole / Volume (dm^3)"

		elif(option1=="mole" and option2=="Volume (dm^3)"):
			res = float(var1)/float(var2)
			eqn = "Equation → concentration(mol/dm^3) = mole / Volume (dm^3)"

		elif(option2=="mole" and option1=="Volume (cm^3)"):
			var1=var1/1000
			res = float(var2)/float(var1)
			eqn = "Equation → concentration(mol/dm^3) = (mole x 1000) / Volume (cm^3)"

		elif(option1=="mole" and option2=="Volume (cm^3)"):
			var2=var2/1000
			res = float(var1)/float(var2)
			eqn = "Equation → concentration(mol/dm^3) = (mole x 1000) / Volume (cm^3)"

		elif (option2=="Molar mass" and option1=="conc (g/dm^3)"):
			res = float(var1)/float(var2)
			eqn = "Equation → concentration(mol/dm^3) = concentration(g/dm^3) / Molar mass"

		elif (option1=="Molar mass" and option2=="conc (g/dm^3)"):
			res = float(var2)/float(var1)
			eqn = "Equation → concentration(mol/dm^3) = concentration(g/dm^3) / Molar mass"

		return render_template('conc.html',res=round(res,2),s=s,eqn=eqn,conc1="mol/dm^3")

@app.route("/molarcalc/nop")
def nop():
	return render_template("nop.html")
@app.route("/molarcalc/nop/result",methods=["POST"])
def nop_result():
	if request.method=='POST':
		
# element = request.form["element"]
		var1 = float(request.form["var1"])
		res=0
		eqn=None
		s="Number of particles = "
		
		res =var1*6

		eqn = "Equation → no of particles  = mole x avogadro constant (6x10^23)"

		return render_template('nop.html',res=round(res,3),s=s,eqn=eqn,nop="particles",x=' x 10^23')



@app.route("/chemcalc")
def chemcalc():
	return render_template("chemcalc.html")
@app.route("/chemcalc/result",methods=["POST"])
def chemcalc_result():
	if request.method=="POST":
		mole = int(request.form["mole"])
		var1 = float(request.form["var1"])
		var2 = float(request.form["var2"])
		option1 = request.form["option1"]
		option2 = request.form["option2"]
		moleproduct = int(request.form["moleproduct"])
		varproduct = float(request.form["varproduct"])
		optionproduct = request.form["optionproduct"]
		res=0
		eqn=None
		s="Mole = "
		if (option1=="mass (g)" and option2=="Molar mass")  :
			res = float(var1) / float(var2)
			eqn = "Equation → Mole = mass / molar mass"
			# return render_template('mole.html',res=res)
		elif (option2=="mass (g)" and option1=="Molar mass"):
			res = float(var2) / float(var1)
			eqn = "Equation → Mole = mass / molar mass"

		elif (option1 == "conc (mol/dm^3)" and option2=="Volume (dm^3)") or (option2 == "conc (mol/dm^3)" and option1=="Volume (dm^3)"):
			res = float(var1)*float(var2)
			eqn = "Equation → mole = concentration (mol/dm^3) x (Volume (cm^3) /1000) "
		elif  (option1 == "conc (mol/dm^3)" and option2=="Volume (cm^3)") :
			var2 = var2/1000
			res = float(var1)* float(var2)
			eqn = "Equation → mole = concentration (mol/dm^3) x Volume (dm^3) "

		elif  (option2 == "conc (mol/dm^3)" and option1=="Volume (cm^3)"):
			var1 = var1/1000
			res = float(var1)* float(var2)
			eqn = "Equation → mole = concentration (mol/dm^3) x (Volume (cm^3) /1000)"

		

		elif (option1 == "avogadro constant (6 x 10^23)" and option2 == "number of particles"):
			res = float(var2)/float(6*10**23)
			eqn = "Equation → mole = no of particles / avogadro constant"
		elif (option2 == "avogadro constant (6 x 10^23)" and option1 == "number of particles"):

			res = float(6*10**23)/float(var2)
			eqn = "Equation → mole = no of particles / avogadro constant"

		elif (option1 == "molar volume constant(24 dm^3)" and option2 == "Volume (dm^3)"):
			res = float(var2)/float(var1)
			eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
		elif (option2 == "molar volume constant(24 dm^3)" and option1== "Volume (dm^3)"):
			res = float(var1)/float(var2)
			eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
		elif (option1 == "molar volume constant(24 dm^3)" and option2 == "Volume (dm^3)"):
			var2=var2/1000
			res = float(var2)/float(var1)
			eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
		elif (option2 == "molar volume constant(24 dm^3)" and option1== "Volume (cm^3)"):
			var1 = var1/1000
			res = float(var1)/float(var2)
			eqn = "Equation → mole = volume(gas) / molar volume constant(24 dm^3) "
		else:
			eqn = "Invalid Input"

		res1 = (moleproduct/mole) * res

		if optionproduct=="Molar mass":
			finalres = res1 * varproduct
			eqn1 = "Equation → Mass = mole x molar mass"
			unit="g"

		elif optionproduct=="conc (mol/dm^3)":
			finalres = res1 / varproduct
			eqn1 = "Equation → volume = mole / concentration (mol/dm^3)"
			unit="dm^3"

		elif optionproduct == "Volume (dm^3)":
			finalres = res1/varproduct
			eqn1 = "Equation → concentration (mol/dm^3) = mole / volume"
			unit = "mol/dm^3"

		elif optionproduct == "Volume (cm^3)":
			varproduct=varproduct/1000
			finalres = res1/varproduct
			eqn1 = "Equation → concentration (mol/dm^3) = mole*1000 / volume"
			unit = "mol/dm^3"

		elif optionproduct=="molar volume constant(24 dm^3)":
			finalres = res1 * 24
			eqn1 = "Equation → volume = mole x molar gas volume"
			unit="dm^3"


		return render_template('chemcalc.html',res=round(res,5),finalres=round(finalres,5),s=s,eqn=eqn,moleproduct=moleproduct,mole=mole,res1=round(res1,3),unit=unit,eqn1=eqn1,s1="mol of the reagent →",s2="mol of the product",s3="1 mol of the reagent →",s4="therefore, mole of the product =",s5='/',s6='*',s7="Result =",s8=')',s9="(")

# @app.route("/balance")
@app.route("/balance")
def balance():
	return render_template("balance.html")
@app.route("/balance/result",methods=["POST"])
def balance_result():
	if request.method=="POST":	
		equation = request.form["s"]
		
		# init_printing(use_unicode=True)

		try:
			def simplify(formula_in):
			    def open_brackets(formula):
			        if formula.find("(") >= 0:
			            formula_br = temp = ""
			            m = 1
			            for i in range(0, len(formula)):
			                if i + 1 < len(formula):
			                    if formula[i].isalpha() and (formula[i + 1].isupper() or formula[i + 1] == "(" or formula[i + 1] == ")"):
			                        temp += formula[i] + "1"
			                    elif formula[i] == ")" and formula[i + 1].isalpha():
			                        temp += formula[i] + "1"
			                    else:
			                        temp += formula[i]
			                else:
			                    if formula[i].isalpha():
			                        temp += formula[i] + "1"
			                    elif formula[i] == ")":
			                        temp += formula[i] + "1"
			                    else:
			                        temp += formula[i]
			            formula = str(temp)
			            for i in range(formula.index(")"), len(formula)):
			                if str(formula[i]).isalpha() or str(formula[i]).isspace() or i == len(formula) - 1:
			                    if (i == len(formula) - 1):
			                        i += 1
			                    formula_br = formula[formula.index("("):i]
			                    break
			            m *= (int(formula_br[formula_br.index(")") + 1:]))
			            val = ""
			            temp = formula_br
			            i = 1
			            while i < temp.index(")") + 1:
			                if temp[i].isdigit():
			                    val += str(temp[i])
			                else:
			                    if len(val) > 0:
			                        temp = temp.replace(
			                            temp[1:i], (temp[1:i - len(val)] + str(int(val) * m)))
			                        val = ""
			                i += 1
			            formula = formula.replace(formula_br, temp[1: temp.index(")")])
			        return formula

			    if formula_in.find(".") >= 0:
			        formula_in = formula_in[0: formula_in.index(
			            ".")] + "." + open_brackets(formula_in[formula_in.index(".") + 1:])
			        d = ""
			        for i in range(formula_in.index(".") + 1, len(formula_in)):
			            if formula_in[i].isdigit():
			                d += formula_in[i]
			            else:
			                break
			        formula_in = formula_in[:formula_in.index(
			            ".")] + open_brackets("(" + formula_in[formula_in.index(".") + len(d) + 1:] + ")" + d)
			    formula_in = open_brackets(formula_in)
			    return formula_in


			def find_lcm(num1, num2):  # function to find the lcm of a list of numbers
			    lcm = int(int(num1 * num2) / int(math.gcd(num1, num2)))
			    return lcm


			def sub_script(s):
			    for i in range(1, len(s)):
			        if s[i].isdigit() and (s[i - 1].isalpha() or s[i - 1] == ")"):
			            s = s[0:i] + s[i].replace("0", "\u2080").replace("1", "\u2081").replace("2", "\u2082").replace("3", "\u2083").replace("4", "\u2084").replace(
			                "5", "\u2085").replace("6", "\u2086").replace("7", "\u2087").replace("8", "\u2088").replace("9", "\u2089") + s[i + 1:]
			    return s


			class compound(object):  # A class of compounds. It stores all the relevant data for the compound
			    def __init__(self, n_compound):
			        self.n_compound = str(n_compound)
			        self.f_compound = simplify((str(n_compound)))
			        temp = ""
			        e = ""
			        v = "0"
			        self.element = []
			        self.val = []
			        for i in range(0, len(self.f_compound) - 1):
			            if self.f_compound[i].isalpha() and self.f_compound[i + 1].isupper():
			                temp += self.f_compound[i] + "1"
			            else:
			                temp += self.f_compound[i]
			        temp += self.f_compound[len(self.f_compound) - 1]
			        if temp[len(temp) - 1].isalpha():
			            temp += "1"
			        self.f_compound = temp
			        for i in range(0, len(self.f_compound)):
			            if self.f_compound[i].isalpha():
			                if v != "0":
			                    if e in self.element:
			                        self.val[self.element.index(e)] = int(
			                            self.val[self.element.index(e)]) + int(v)
			                    else:
			                        self.element.append(str(e))
			                        self.val.append(int(v))
			                    e = self.f_compound[i]
			                    v = "0"
			                    i -= 1
			                else:
			                    e += self.f_compound[i]
			            elif self.f_compound[i].isdigit():
			                v += self.f_compound[i]

			        if e in self.element:
			            self.val[self.element.index(e)] = int(
			                self.val[self.element.index(e)]) + int(v)
			        else:
			            self.element.append(str(e))
			            self.val.append(int(v))


			# equation = str(input("Enter a chemical equation: "))

			equation = equation.replace("=", "+").replace(' ', '')
			compounds = []  # An array of compounds
			elements = []  # An array of all the elements present in the equation

			# Assigning a compound name to an object of the class compound and storing it in the array
			for i in range(0, len(equation.split("+"))):
			    compounds.append(compound(equation.split("+")[i]))
			# Checking if element has already been added to the 'elements' array. Addidng it if it has not been added
			for i in range(0, len(compounds)):
			    for x in range(0, len(compounds[i].element)):
			        if not(compounds[i].element[x] in elements):
			            elements.append(compounds[i].element[x])

			# Number of columns in the matrix. There is one column for every compound in the equation
			cols = len(compounds)
			# Number of rows in the matrix. There is one row for every element in the equation
			rows = len(elements)
			m = (zeros(rows, cols))

			# The number of atoms of an element present in a particular compound is stored in the matrix
			for c in range(0, int(cols)):
			    for r in range(0, int(rows)):
			        try:
			            m[r, c] = compounds[c].val[compounds[c].element.index(elements[r])]
			        except:
			            m[r, c] = 0

			# print(m)
			# print("\nRREF Matrix:\n")
			# print(m.rref())
			m = (list(m.rref()))[0]  # The matrix is converted to Row Reduced Echelon Form

			coefficients = []  # Array to store the coefficients of the compounds
			denominator = []  # Array to store the denominator of the coefficients of the compounds

			for r in range(0, rows):
			    if str(m[r, cols - 1]) == "0":
			        break
			    elif str(m[r, cols - 1]).find("/") > 0:
			        coefficients.append(int(str(m[r, cols - 1]).split("/")[0]))
			        denominator.append(int(str(m[r, cols - 1]).split("/")[1]))
			    else:
			        coefficients.append(int(str(m[r, cols - 1])))
			        denominator.append(1)
			coefficients.append(int(m[0, 0]))
			denominator.append(1)


			# LCM of the denominators is calculated
			lcm = find_lcm(int(denominator[0]), int(denominator[1]))
			for i in range(2, len(denominator)):
			    lcm = find_lcm(lcm, denominator[i])

			x = 0
			# The coefficients are multiplied by the LCM
			for i in range(0, len(coefficients)):
			    if coefficients[i] < 0:
			        x += 1
			    if x > 1:
			        coefficients[i] = abs(coefficients[i])
			    coefficients[i] = int(coefficients[i] * lcm / denominator[i])

			equation = ""

			# Concatenating the coefficients and the molecular formula of the compounds
			for i in range(0, len(compounds)):
			    if coefficients[i] < 0:
			        equation = equation.strip()[:-2].strip() + " \u2794 "
			    equation += (str(abs(coefficients[i])) if (abs(coefficients[i])) > 1 else "") + \
			        "" + sub_script(compounds[i].n_compound)
			    if not(i == len(compounds) - 1):
			        if len(compounds)==3 and i==1:
			            equation += " \u2794 "
			        else:	
			            equation += " + "
			result = equation
		except IndexError:
			result = "Invalid Equation"
		return render_template("balance.html",result=result)

@app.route("/periodic")
def period():
	

	return render_template("periodic.html")

		
if __name__ == "__main__":
    app.run(debug=True)