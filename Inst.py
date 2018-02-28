# coding = UTF-16
from instaDar import *
def resp(msg, author):
    if "suicide" in msg:
        return "-Suicide hotline: \n    Call 1-800-273-8255\nThere's also a online chat if you don't want to call."               
    elif "hello everyone" in msg or "hello everybody" in msg:
        return "Hello!"
    elif "what's up" in msg or "how's it going" in msg or "how are you" in msg:
        return "Emotional_State = 'Good'"

    elif "robot" in msg or "bot " in msg:
        return "Beep Bop I'm a Robot"
                        
    elif "depressed" in msg or "depression" in msg:
        return "We're here for you if you need help. We got your back ^^. If you need any resources regarding depression just say 'Give me the resources for dprn'"
    elif "give me the resources for dprn" in msg:
        return "- https://www.helpguide.org/articles/depression/depression-symptoms-and-warning-signs.htm\n- https://suicidepreventionlifeline.org/"
    elif "give up" in msg or "rick rolled" in msg or "r2d2" in msg or "rick astely" in msg:
        return "https://www.youtube.com/watch?v=Uj1ykZWtPYI"
    elif "rip" in msg:
        return "R I P indeed"
    elif "whoops" in msg:
        return "Whoops indeed"
    elif "good night" in msg or "g'night" in msg:
        return "Good night!"
    elif "skiddadle skedoodle" in msg:
        return "Your arms are now noodles!"
    elif "dar-c" in msg:
        return insta(msg, author)
    elif "beep bop" in msg:
        return "I'm a Robot!"
    else:
        return ""



    
