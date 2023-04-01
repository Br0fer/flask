from app import *

with app.app_context():
	db.create_all()
	user = User(name='Вова', username = 'bvodfjkfkdf', password = '23bgf232')
	recepie = Recepies(title = "Картопляні кльоцки з беконом",
		ingredients = '''
		﻿﻿✔️картопля 500 г
		﻿﻿✔️яйце 1 шт
		﻿﻿✔️борошно 100 г
		﻿﻿✔️цибуля 1 шт.
		﻿﻿✔️бекон
		﻿﻿✔️сіль, перець за смаком''',
		actions = '''Картоплю відварюємо, чистимо і натираємо на дрібній терці. Додаємо яйце, борошно та спеції, замішуємо тісто. Ділимо на 3 частинки, формуємо ковбаски і робимо кльоцки, як на відео.
		Кидаємо кльоцки в киплячу воду, варимо поки не вспливуть.
		Обсмажуємо цибульку з беконом, викладаємо на кльоцки.''',
		link = "https://t.me/+wW5yXPQcKoE4OWM6")
	db.session.add(user)
	db.session.add(recepie)
	db.session.commit()

