#CHARACTERS

define config.developer = True

define c = Character("Cirno")

define reimu = Character("Reimu")

define remi = Character("Remilia")

define s = Character("Sakuya")

define p = Character("Patchouli")

define m = Character("Moka")

define y = Character("Yukari")
define h = Character("Hong")
define bikini = Character("Girl in bikini")
define sundress = Character("Girl in sundress")
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
