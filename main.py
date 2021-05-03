from segno import helpers

qr = helpers.make_mecard(
    name="Douglas Bianchezzi",
    email="a@a.com",
    phone="+55(11)11111 1111",
    country="america"
)

qr.save("visit_card.png", scale=10)