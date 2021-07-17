from django.shortcuts import render
from random import randint


def home(request):
	return render(request, 'home.html', {})

def add(request):

	num_1 = randint(1, 10)
	num_2 = randint(1, 10)

	if request.method == "POST":
		answer = request.POST['answer']
		
		if not answer:
			context = {
				'message': "You did not supply an answer!",
				'color': "warning",
				'num_1': num_1, 
				'num_2': num_2,
			}

			return render(request, 'add.html', context)

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) + int(old_num_2)

		if int(answer) == correct_answer:
			message = f"Correct! {old_num_1} + {old_num_2} is {answer}."
			color = "success"
		else:
			message = f"Incorrect! {old_num_1} + {old_num_2} is not {answer}. {old_num_1} + {old_num_2} is {correct_answer}."
			color = "danger"

		context = {
			'answer': answer,
			'message': message,
			'color': color,
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'add.html', context)
	else:
		context = {
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'add.html', context)

def subtract(request):

	num_1 = randint(1, 10)
	num_2 = randint(1, 10)

	if request.method == "POST":
		answer = request.POST['answer']
		
		if not answer:
			context = {
				'message': "You did not supply an answer!",
				'color': "warning",
				'num_1': num_1, 
				'num_2': num_2,
			}

			return render(request, 'subtract.html', context)

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) - int(old_num_2)

		if int(answer) == correct_answer:
			message = f"Correct! {old_num_1} - {old_num_2} is {answer}."
			color = "success"
		else:
			message = f"Incorrect! {old_num_1} - {old_num_2} is not {answer}. {old_num_1} - {old_num_2} is {correct_answer}."
			color = "danger"

		context = {
			'answer': answer,
			'message': message,
			'color': color,
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'subtract.html', context)
	else:
		context = {
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'subtract.html', context)

def multiply(request):
	
	num_1 = randint(1, 10)
	num_2 = randint(1, 10)

	if request.method == "POST":
		answer = request.POST['answer']
		
		if not answer:
			context = {
				'message': "You did not supply an answer!",
				'color': "warning",
				'num_1': num_1, 
				'num_2': num_2,
			}

			return render(request, 'multiply.html', context)

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) * int(old_num_2)

		if int(answer) == correct_answer:
			message = f"Correct! {old_num_1} x {old_num_2} is {answer}."
			color = "success"
		else:
			message = f"Incorrect! {old_num_1} x {old_num_2} is not {answer}. {old_num_1} x {old_num_2} is {correct_answer}."
			color = "danger"

		context = {
			'answer': answer,
			'message': message,
			'color': color,
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'multiply.html', context)
	else:
		context = {
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'multiply.html', context)

def divide(request):
	
	num_1 = randint(1, 10)
	num_2 = randint(1, 10)

	if request.method == "POST":
		answer = request.POST['answer']
		
		if not answer:
			context = {
				'message': "You did not supply an answer!",
				'color': "warning",
				'num_1': num_1, 
				'num_2': num_2,
			}

			return render(request, 'divide.html', context)

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) // int(old_num_2)

		if float(answer) == correct_answer:
			message = f"Correct! {old_num_1} // {old_num_2} is {answer}."
			color = "success"
		else:
			message = f"Incorrect! {old_num_1} // {old_num_2} is not {answer}. {old_num_1} // {old_num_2} is {correct_answer}."
			color = "danger"

		context = {
			'answer': answer,
			'message': message,
			'color': color,
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'divide.html', context)
	else:
		context = {
			'num_1': num_1, 
			'num_2': num_2,
		}

		return render(request, 'divide.html', context)

