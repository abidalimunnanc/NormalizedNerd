from manimlib.imports import *

class Scene1(Scene):
  def construct(self):

  	line1 = TexMobject("\\text{features: }", "X = (X_1, X_2,...,X_n)")
  	line2 = TexMobject("\\text{label: }", "Y")
  	self.play(Write(line1))
  	self.wait()
  	self.play(ApplyMethod(line1.shift,.5*UP))
  	line2.shift(.5*DOWN)
  	self.play(Write(line2))
  	self.wait()
  	gr=VGroup(line1,line2)
  	self.play(FadeOut(gr))
  	self.wait()
  	line3 = TexMobject("P(Y=y | X = (x_1, x_2,...,x_n))")
  	self.play(Write(line3))
  	self.wait()
  	line4 = TextMobject("for what value of ", "$y$")
  	line4.shift(UP)
  	line5 = TextMobject("is maximum")
  	line5.shift(DOWN)
  	self.play(Write(line4))
  	self.play(Write(line5))
  	self.wait()
  	gr=VGroup(line3,line4,line5)
  	self.play(FadeOut(gr))
  	line1 = TexMobject("\\text{but...}", "P(Y|X)", "\\text{ is hard to find!}")
  	self.play(Write(line1))
  	self.wait()
  	self.play(FadeOut(line1))
  	line1 = TexMobject("P(Y|X) = ", "{P(X|Y)", "P(Y)", "\\over", "P(X)}")
  	line1[0].set_color(GREEN)
  	line1[2].set_color(BLUE)
  	line1[4].set_color(YELLOW)
  	line1[1].set_color(RED)
  	self.play(Write(line1))
  	ptr1 = CurvedArrow(5*LEFT+1*UP, 3*LEFT)
  	txt1 = TextMobject("Posterior").set_color(GREEN)
  	txt1.shift(5*LEFT+1.5*UP)
  	ptr2 = CurvedArrow(2*UP+4*RIGHT, 2.5*RIGHT+.8*UP)
  	txt2 = TextMobject("Prior").set_color(BLUE)
  	txt2.shift(2*UP+5*RIGHT)
  	ptr3 = CurvedArrow(3.5*RIGHT+2*DOWN, 1.5*RIGHT+.8*DOWN, angle=-PI/2)
  	txt3 = TextMobject("Evidence").set_color(YELLOW)
  	txt3.shift(5*RIGHT+2*DOWN)
  	ptr4 = CurvedArrow(1*LEFT+2*UP, .25*LEFT+.6*UP)
  	txt4 = TextMobject("Likelihood").set_color(RED)
  	txt4.shift(1*LEFT+2.5*UP)
  	self.play(Write(ptr1))
  	self.play(Write(txt1))
  	self.wait()
  	self.play(Write(ptr2))
  	self.play(Write(txt2))
  	self.wait()
  	self.play(Write(ptr3))
  	self.play(Write(txt3))
  	self.wait()
  	self.play(Write(ptr4))
  	self.play(Write(txt4))
  	self.wait()
  	self.play(ApplyMethod(line1[4].set_color, GREY))
  	self.wait()



class Scene2(Scene):
    def construct(self):
        tabledict={
            "X_1":['0', '0', '1', '0', '2', '1', '0', '2', '2', '1'],
            "X_2":['0', '1', '2', '0', '2', '1', '2' ,'0', '1', '0'],
            "Y ":['0', '1', '1', '1', '0', '0', '1', '0', '0', '0'],
        }

        table=Table.get_table(tabledict)
        table.move_to(ORIGIN)
        table.scale(.6)
        self.play(Write(table), run_time=3)
        self.wait()

        descx = TexMobject("X_1, X_2 \\in \\{0, 1, 2\\}")
        descy = TexMobject("Y \\in \\{0, 1\\}").next_to(descx, DOWN)

        gdesc = VGroup(descx, descy)
        gdesc.scale(.6)
        gdesc.shift(3.5*RIGHT)
        self.play(Write(gdesc))
        self.wait()

        self.play(FadeOut(gdesc))

        self.play(ApplyMethod(table.shift,5*RIGHT))
        self.wait()

        prob = TexMobject("\\text{Estimate the value of }", "Y",  "\\text{given that }", "X = (0, 2)")
        prob.scale(.7)
        prob.shift(3*LEFT)
        self.play(Write(prob))
        self.wait()
        self.play(FadeOut(prob))
        self.wait()

        line1 = TexMobject("\\text{Let's compute }", "P(Y=0|X=(0, 2))", "\\text{ and }", "P(Y=1|X=(0, 2))", "\\text{ ... }")
        line1.to_edge(UP, buff=.2)
        line1.shift(2.8*LEFT)
        line1.scale(.6)
        self.play(Write(line1))
        self.wait()

        line2 = TexMobject("P(Y=0) = ", "{\#Y=0", "\\over", "\#Y=0", "+", "\#Y=1}")
        line2.next_to(line1, DOWN)
        line2.scale(.6)
        self.play(Write(line2))
        self.wait()

        gr = VGroup(table[23],table[27],table[28], table[30], table[31], table[32])
        self.play(ApplyMethod(gr.set_color, RED))
        g = VGroup(line2[1], line2[3])
        self.play(ApplyMethod(g.set_color, RED))
        self.wait()

        gr1 = VGroup(table[24],table[25],table[26], table[29])
        self.play(ApplyMethod(gr1.set_color, BLUE))
        self.play(ApplyMethod(line2[5].set_color, BLUE))
        self.wait()

        line3 = TexMobject("= \\frac{6}{10}")
        line3.scale(.6)
        line3.next_to(line2)
        self.play(Write(line3))
        self.wait()
        line4 = TexMobject("P(Y=1) = ", "{\#Y=1", "\\over", "\#Y=0", "+", "\#Y=1}")
        line4.next_to(line2, DOWN)
        line4.scale(.6)
        self.play(Write(line4))
        self.wait()
        
        gr2 = VGroup(line4[1], line4[5])
        self.play(ApplyMethod(gr2.set_color, BLUE))
        self.play(ApplyMethod(line4[3].set_color, RED))
        self.wait()
        line5 = TexMobject("= \\frac{4}{10}")
        line5.scale(.6)
        line5.next_to(line4)
        self.play(Write(line5))
        self.wait()

        line6 = TexMobject("P(X=(0,2)|Y=1)")
        line6.scale(.6)
        line6.next_to(line4.get_corner(DOWN+LEFT),DOWN, buff=.7)
        self.play(Write(line6))
        self.wait()
        
        gr3 =  VGroup(table[9], table[19], table[29]) 
        framebox1 = SurroundingRectangle(gr3, buff=.1)
        self.play(Write(framebox1))
        self.wait()
        

        line7 = TexMobject("= \\frac{1}{4}")
        line7.scale(.6)
        line7.next_to(line6)
        self.play(Write(line7))  
        self.play(FadeOut(framebox1))
        self.wait()

        line8 = TexMobject("P(X=(0,2)|Y=0)")
        line8.scale(.6)
        line8.next_to(line6, DOWN, buff=.5)
        self.play(Write(line8))
        self.wait()

        line9 = TexMobject("= 0")
        line9.scale(.6)
        line9.next_to(line8)
        self.play(Write(line9))
        self.wait()

        line10 = TexMobject("P(X=(0,2)|Y=0) * P(Y=0)")
        line10.scale(.6)
        line10.next_to(line8, DOWN, buff=.7)
        line10.shift(.71*RIGHT)
        self.play(Write(line10))
        self.wait()

        line11 = TexMobject("P(X=(0,2)|Y=1) * P(Y=1)")
        line11.scale(.6)
        line11.next_to(line10, DOWN, buff=.5)
        self.play(Write(line11))
        self.wait()

        line12 = TexMobject("= 0* \\frac{6}{10} =", "0")
        line12[1].set_color(GREEN)
        line12.scale(.6)
        line12.next_to(line10)
        self.play(Write(line12))
        self.wait()

        line13 = TexMobject("= \\frac{1}{4} * \\frac{4}{10} =", "\\frac{1}{10}")
        line13[1].set_color(ORANGE)
        line13.scale(.6)
        line13.next_to(line11)
        self.play(Write(line13))
        self.wait()

        gr4 = VGroup(line10, line11, line12, line13)

        line14 = TexMobject("\\text{Estimated value of }", "Y", "\\text{ is }",  "1", "\\text{ given }", "X=(0,2)")
        line14.scale(.7)
        line14.next_to(line8, DOWN, buff=.7)
        line14.move_to(gr4)
        self.play(Transform(gr4, line14))
        self.wait()

        line15 = TexMobject("\\text{Let's assume }", "X_1, X_2", "\\text{ are independant! }")
        line15.scale(.8)
        line15.move_to(line14)
        self.play(Transform(gr4, line15))
        self.wait()

        self.play(FadeOut(gr4))

        line16 = TexMobject("= P(X_1=0|Y=1) * P(X_2=2|Y=1)").set_color(GREEN)
        line16.scale(.6)
        line16.next_to(line6)
        self.play(FadeOut(line7))
        self.play(Write(line16))
        self.wait()

        line17 = TexMobject("= P(X_1=0|Y=0) * P(X_2=2|Y=0)").set_color(PURPLE)
        line17.scale(.6)
        line17.next_to(line8)
        self.play(FadeOut(line9))
        self.play(Write(line17))
        self.wait()

        arrow1 = Arrow(LEFT,RIGHT)
        arrow1.scale(.5)
        arrow1.next_to(table[6], LEFT)
        arrow2 = Arrow(LEFT,RIGHT)
        arrow2.scale(.5)
        arrow2.next_to(table[4], LEFT)
        arrow3 = Arrow(LEFT,RIGHT)
        arrow3.scale(.5)
        arrow3.next_to(table[9], LEFT)
        gr5 = VGroup(arrow2, arrow1, arrow3)
        gr5.set_color(YELLOW)
        self.play(Write(gr5))
        self.wait()

        line18 = TexMobject("= \\frac{3}{4}").set_color(GREEN)
        line18.scale(.6)
        line18.next_to(line16)
        self.play(Transform(gr5, line18))
        self.wait()

        arrow1 = Arrow(LEFT,RIGHT)
        arrow1.scale(.5)
        arrow1.next_to(table[15], LEFT)
        arrow2 = Arrow(LEFT,RIGHT)
        arrow2.scale(.5)
        arrow2.next_to(table[19], LEFT)
        gr6 = VGroup(arrow1, arrow2)
        gr6.set_color(YELLOW)
        self.play(Write(gr6))
        self.wait()

        line19 = TexMobject(" \\frac{2}{4}").set_color(GREEN)
        line19.scale(.6)
        line19.next_to(gr5)
        self.play(Transform(gr6, line19))
        self.wait()

        arrow1 = Arrow(LEFT,RIGHT)
        arrow1.scale(.5)
        arrow1.next_to(table[3], LEFT)
        arrow1.set_color(YELLOW)
        self.play(Write(arrow1))
        self.wait()

        line20 = TexMobject("= \\frac{1}{6}").set_color(PURPLE)
        line20.scale(.6)
        line20.next_to(line17)
        self.play(Transform(arrow1, line20))
        self.wait()

        arrow2 = Arrow(LEFT,RIGHT)
        arrow2.scale(.5)
        arrow2.next_to(table[17], LEFT)
        arrow2.set_color(YELLOW)
        self.play(Write(arrow2))
        self.wait()

        line21 = TexMobject(" \\frac{1}{6}").set_color(PURPLE)
        line21.scale(.6)
        line21.next_to(line20)
        self.play(Transform(arrow2, line21))
        self.wait()

        line22 = TexMobject(" \\frac{3}{4} * \\frac{2}{4}", ">",  "\\frac{1}{6} * \\frac{1}{6}")
        line22[0].set_color(GREEN)
        line22[2].set_color(PURPLE)
        line22.scale(.6)
        line22.shift(1.6*DOWN+2*LEFT)
        self.play(Write(line22))
        self.wait()

        line23 = TexMobject("\\text{So, the estimated value of }", "Y", "\\text{ is }", "1")
        line23.scale(.6)
        line23.next_to(line22, DOWN)
        self.play(Write(line23))
        self.wait(2)



class Scene3(Scene):
    def construct(self):
    	 line = TextMobject("Dealing with Continuous features").set_color(RED)
    	 line.to_corner(LEFT+UP)
    	 self.play(Write(line))
    	 self.wait()
    	 line1 = TextMobject("1. Discretization").scale(.7).next_to(line, DOWN, buff=.6)
    	 self.play(Write(line1))
    	 self.wait()
    	 line3 = TexMobject("age \\in (11, 50)", "\\longrightarrow", "age \\in \\{1, 2, 3, 4\\}").scale(.7).next_to(line1, DOWN)
    	 line3[0].set_color(GREEN)
    	 line3[2].set_color(BLUE)
    	 self.play(Write(line3[0]))
    	 self.wait()
    	 self.play(Write(line3[1]))
    	 self.play(Write(line3[2]))
    	 self.wait()
    	 line2 = TextMobject("2. Fit a known Distribution").scale(.7).next_to(line1, DOWN, buff=3)
    	 self.play(Write(line2))
    	 self.wait()
    	 line4 = TexMobject("P(X=(x_1, x_2,...,x_n)|Y=y)", "=", "\\prod{}{} f(X_i=x_i|Y=y)").scale(.7).next_to(line2, DOWN)
    	 line4[0].set_color(GREEN)
    	 line4[2].set_color(BLUE)
    	 line4.shift(RIGHT)
    	 self.play(Write(line4[0]))
    	 self.wait()
    	 self.play(Write(line4[1]))
    	 self.play(Write(line4[2]))
    	 self.wait()


























		 
		 	
    	
    	