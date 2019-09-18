#CHARACTERS

define config.developer = True

define c = Character("Cirno", who_color = "#41B0F8", what_color="#41DCF8")

define reimu = Character("Reimu", who_color="#F11212", what_color="#FFFFFF")

define remi = Character("Remilia", who_color="#F11212", what_color="#FFDAFA")

define s = Character("Sakuya", who_color="#818FFF", what_color="#CCCCCC")


define m = Character("Moka", who_color="#FE5463", what_color="#FC60E5")

define y = Character("Yukari", who_color="#FFE318", what_color="#C8B5FF")
define h = Character("Hong", who_color="#FF5555", what_color="#C9E29A")
define bikini = Character("Girl in bikini", who_color="#3AF72A", what_color="#C95D5D")
define sundress = Character("Girl in sundress", who_color="#EA54D3", what_color="#F7D3F2")
define cirno_scale = 0.6
define moka_scale = 0.85
define sakuya_scale = 1.05
define bikini_scale = 1.2
define sun_scale = 1.2
#IMAGES

image cirno summer happy = im.FactorScale("cirno_summer_happy.png", cirno_scale)
image cirno summer surprise = im.FactorScale("cirno_summer_surprise.png", cirno_scale)
image moka interested = im.FactorScale("moka interested.png",moka_scale)
image moka oof = im.FactorScale("moka oof.png", moka_scale)
image moka happy = im.FactorScale("moka happy.png", moka_scale)
image moka smile = im.FactorScale("moka smile.png", moka_scale)
image sakuya happy = im.FactorScale("sakuya happy.png", sakuya_scale)
image sakuya surprise = im.FactorScale("sakuya surprise.png",sakuya_scale)
image sakuya sigh = im.FactorScale("sakuya sigh.png", sakuya_scale)
image sakuya mad = im.FactorScale("sakuya mad.png", sakuya_scale)
image sakuya smile = im.FactorScale("sakuya smile.png", sakuya_scale)
image sakuya sweat = im.FactorScale("sakuya sweat.png", sakuya_scale)
image sakuya tear = im.FactorScale("sakuya tear.png", sakuya_scale)
image sun_dress = im.FactorScale("sun_dress.png", bikini_scale)
image bikini_girl = im.FactorScale("bikini_girl.png", sun_scale)
