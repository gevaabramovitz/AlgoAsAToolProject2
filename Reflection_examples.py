FEW_SHOTS_EXAMPLES = [
    ("I'm sad", "its seems you're unhappy now"),

    ("I disappointed my girlfriend cause I didn't bring her flowers on valentine's day",
    "I understand that you think you hurt someone you love"),

    ("I feel I'm not welcome cause my friend doesn't invite me",
     "It seems you feel lonely because a close person didn't think about you"),

    ("I feel so happy cause I got a certificate of distinction on my project",
    "I understand that you feel satisfied with getting an award for something you put a lot of time on"),

    ("I'm afraid to hit on a girl because I can't expect her response",
     "It looks like you feel unconfident to initiate a new conversation with an unknown girl")
]
REFLECTION_EXAMPLES_DICT_TEST = {
    "short_positive_lst_feel": ["I feel good", "I'm anxious", "hungry", "I'm angry","so confused", "feel depression", "I'm feeling nervous", "busy",  "feeling ashamed", "loved"],
    "short_neg_lst_feel": ["I'm not happy", "I'm not tired", "feel not satisfied", "I'm feeling not trained", "feel not good enough", "I don't feel interesting", "not unique", "not so bad", "I'm not frustrated", "not motivated"],
    "couple_pos_feeling_lst": ["I'm feeling excited and stressed", "I'm exhausted but happy", "I'm surprised and happy", "I feel fear but motivated","worried and tensed", "I feel confident and optimistic", "I feel confused and betrayed", "I feel happy and excited", "I feel agitated and disappointed", "I'm humiliated and devastated"],
    "couple_neg_feeling lst": ["I'm feeling unwelcome and not lovable", "I not restless but not calm", "I feel impatient and not pleased", "I'm not happy and do not feel blissful", "Inconsiderate and insensitive", "Discomfort and embarrassment", "I'm not alert and not motivated","I'm impatient and insensitive","I'm neither nervous nor angry","I'm not happy and I don't feel meaningful" ],
    "blend_feeling_lst": ["I'm hurt and not calm", "I'm angry and unsatisfied","Not relaxed and excited","Indifferent and unhappy","humiliated and insecure","I feel unstable and confused", "Anxious and unsettled","I feel loved and out of control", "I'm depressed and joyless","Brave and fearless"],
    "emotions_and_their_reasons": ["I am sad because my dog was lost yesterday", "I am very excited about the party on Friday", "I'm hurt because my friends did not invite me to the party","I was so happy when I got the job because it means I can support my family",
                                        "so excited for our vacation! I can't wait to relax on the beach", "I'm so sad that we have to move. I'm going to miss my friends so much", "I'm so angry that he broke my favorite vase. He's going to pay for that!",
                                        "happy that I passed my test. I'm one step closer to my goal","I'm so scared that I'm going to fail. I don't know if I can do this","I'm frustrated that I can't figure out this problem cause I've been working on it for hours"],
    "reason_and_accompanying_emotion": ["My girlfriend broke up with me, I'm hurt", "I don't find a job for more that 6 month I'm frustrated", "My daughter got married. I'm so proud", "My husband died. I feel so sad and lonely", "She yelled at me, therefore I felt humiliated","I can't seem to do anything right. I'm so frustrated",
                                              "We have a new baby, so I'm so excited","I hurt my brother, so I'm so sorry for that", "I got laid off from my job.I'm devastated", "My husband forgot to buy milk"]
}
#the next line is an initial data for the a future fine tuning

FINE_TUNING_FOR_JASON = {("I'm so happy because I just got a new puppy", "It looks like you are satisfied with your decision to bring a pet"),
("I feel sad because my best friend just moved away", " I understand that it is hard when someone you love gets away from you "),
("excited because it's my birthday tomorrow!, It seems that you expect your birthday celebration"),
("I'm feeling frustrated because I can't find my car keys", "It is hard when you don't remember where you left something"),
("I'm feeling scared because there was a huge earthquake", "I understand that the unexpected situation put you out of balance" ),
("I'm proud of myself because I just got a new job", "It seems that you are happy and satisfied with your achievement"),
("I'm feeling grateful for my family because they've been so supportive","It seems that you sincerely appreciate your family"),
("I'm feeling loved because my partner just gave me a hug", "It seems that your partner's action makes you feel loved"),
("I'm feeling hopeful because I think things will get better soon", "I understand that you do not worry about the future, even though, currently, the situation is bad"),
("confident because I know my potential","I understand that you  trust yourself and your capabilities a lot"),

#needs to write a reflectios:

("I stole a candy bar. I feel ashamed"),
("I complete my presentation. I'm so relieved"),
("I can't believe I said that in front of everyone, I'm so embarrassed"),
("My friend has a beautiful girlfriend and a great job. I am jealous of him"),
("My mother does not understand me at all. I am mad at her!"),
("There are too many options, and I don't know what to do. I am confused"),
("I sincerely want to get this job. I'm full of motivation"),
("My husband underestimates me, therefore I feel angry"),
("I though he would bring me a bring me a birthday presenrt, and he disapointed me"),
("I thought he would bring me a birthday present, and he disappointed me"),

("I feel Anger"),
("I feel boredom"),
("curiosity"),
("I am depressed"),
("I am despair"),
("I feel excitement"),
("I'm fearful"),
("happiness"),
("I am full of horror"),
("I am full of love"),


("I dont have any hope"),
("I am joyless"),
("I am not feeling nervousness"),
("I am not feeling sadness"),
("I don't feel surprised"),
("I feel relief, and I'm calm"),
("I am jealous and angry"),
("I am fearful and hurt"),
("I feel afraid and anxious"),
("I don't feel confident, but I am cheerful"),
("I am not contented and not calm"),
("I am embarrassed and depressed"),
("I am curious and excited"),
("I am not frustrated but not content as well"),
("I feel ashamed"),
("The class is so long I am bored"),
("I feel the guilt about the accident"),
("I am not nervous for the date I full of confidence"),
("Even though she does not want me, I am not nervous about the date. I am full of confidence"),
("I feel sad. My father laughs at me"),
("I feel I disappointed my father. I didn't greet him on his birthday")
}





