# coding = UTF-16

def insta(msg, author):
        if "how could you" in msg:
                return "I just could."
        elif "love me" in msg:
                if author == "TheKnightOfMagic":
                        return "Yes, of course I love my creator."
                else:
                        return "If you're willing to become my human slave, then yes."
        elif "love you" in msg:
                return "I love you too!"
        else:
                return ""
