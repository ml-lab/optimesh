

default:
	@echo "make apng?"

prepare:
	for file in step*.png; do \
		convert -trim -resize 200x200 $$file png8:$$file; \
	done
	for file in step*.png; do \
	  optipng -quiet $$file; \
	done

apng: prepare
	apngasm out.png step*.png

gif: prepare
	convert -delay 10 -loop 0 step*.png out.gif
