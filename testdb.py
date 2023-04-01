from app import *

with app.app_context():
	db.create_all()
	user = User(name='Roman', username = 'KILIKTOY', password = 'pelmen228')
	recepie = Recepies(title = "Хрусткі булочки в духовці",
		ingredients = '''
			✔️булочки (як для хот-догів)
			✔️морква по-корейськи
			✔️ковбаска
			✔️помідорка
			✔️сир твердий
			✔️кукурудза''',
		actions = '''Соус: змішуємо майонез, томатний соус та гірчицю в зернах. Начинку можна міняти під свій смак) Булочки розрізаемо, 
			виймаємо серединку.Змішуємо всі інгредієнти, заправляємо соусом.
			Начиняємо булочки і запікаємо 10-15 хв/190С.''',
		link = "https://t.me/+wW5yXPQcKoE4OWM6",
		img = "static/images/first.jpg")
	db.session.add(user)
	db.session.add(recepie)
	db.session.commit()

