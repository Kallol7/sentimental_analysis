import config
import cohere
from cohere.classify import Example


def classify(data_f,strt,end):
    df=data_f.copy()
    reviews=df['review'].to_list()
    reviews=reviews[strt:end]

    sentiments= df['sentiment'].to_list()
    sentiments=sentiments[strt:end]
    # print(reviews)

    co = cohere.Client(config.API_KEY)


    ##blockPrint()

    #input can not be empty
    if len(reviews)==0:
        return [],[]

    classifications = co.classify(
    model='medium',
    taskDescription='',
    outputIndicator='',
    
    # inputs=["Sure,\n  it\'s a nice beach, but I maybe expected more. We had to pay $35 for parking\n and then saw that we probably could have found street parking and walked. If\n  you plan to swim and use the beach, it\'s probably good for that, but not\n  worth the parking cost it if just passing through."
    # , 
    # "Sandy\n  white beaches!!! Clean and free of trash these beaches are always an amazing\n  experience. The water is gorgeous and often times you have nice sand bars\n  that allow you to go out further. This time around we had many manta rays\n  swimming around which adds to the beauty. A must see!"
    # ,
    # "Twice\n  we drove all the way down to the coast and bought hotel rooms for multiple\n  nights hoping to see one of the turtle releases and twice the National\n  Seashore underachieved.\n    The beach is beautiful however I am incredibly disappointed in the turtle\n  release program they have! They state on their website to plan your trip\n  around the time the most turtles are expected to hatch.\n    My family and I went down to the coast to watch the turtles hatch.... Well\n  you can imagine our disappointment when no public releases happened.\n    We later found out that the turtles did hatch they simply didn’t want to\n  host a PUBLIC release even though we planned for the dates that coincided\n  with the release dates on their website."],

    inputs= reviews,

    examples=[
        Example("Most\n  people turn at the Navarre Beach sign and drive straight to the beach.\n  However, it is a long walk to the pier and a long walk to the water. If you\n  don\'t want a long walk to the beach, drive a few minutes west and look for\n  area 29, 32, or 33. We went in August. If you are looking for a relaxing ,\n  family beach, this is it!", "positive"), 
        Example("Gorgeous\n  beach. Navarre is beautiful and the sand is super soft. It’s a clean beach\n  and very family friendly which is awesome. It’s also nice that there isn’t\n  much built up around it but maybe 4 condos/ 1 hotel. The only downside was\n  the lack of good restaurants. The food across the board was average and lots\n  of fried food but healthy options were tough to find. This is definitely a\n  beach only destination which is completely fine by me. I love that there\n  aren’t beach superstores, chains everywhere next to the beach. I love that\n  it’s more quiet than the really populated beaches like Panama City Beach,\n  Miami, Daytona, etc. Go with Navarre or the beaches down south if you’re\n  looking for a more relaxed spot", "positive"), Example("Nice Long\n  Beach, with good drive on access points. Was windy and cool when we were\n  there but still had a nice relaxing day there.", "positive"), Example("We love\n  the big beaches in Wildwood. They are clean, friendly, dogs can hang out, and\n  plenty of room to play games. We love this place.", "positive"), Example("the beach\n  was clean. we brought our Golden to the part that was dog friendly. He did\n  not care for the waves and would not go very far in but i still had a nice\n  time.", "positive"), Example("We\n  have been to Poipu beach twice. Both times it was very crowded and dirty. If\n  you go, bring some shade, there is not much shade to be had here. Good for\n  snorkeling if you don’t mind the crowds. There are restrooms with changing\n  rooms that are relatively clean considering the amount of use. We heard about\n  Anini beach on the North Shore, and liked it much better.", "negative"), Example("Apparently\n  this is \"America\'s best beach\"? Who are these Americans??! All I\n  saw was Midwestern tourists wearing trucker hats and screaming at their kids\n  and each other. Maybe it\'s great for families- but as a solo traveler, this\n  place actually disturbed my peace! I made a special trip south to see it, and\n  lasted maybe 40 mins before I HAD TO leave. Too busy, crowded, populated and\n  touristy. Not the real Hawaii- like Coney Island of the pacific!", "negative"), Example("First\n  visit stopped in for a late dinner. Place is clean, service was good. We\n  ordered Banging shrimp for our appetizer. Frozen fried shrimp with hot\n  sauce🙄🙄. For our main course, fish tacos an a burger an\n  fries. The burger was paper thin an cooked black it was so hard my husband\n  could not eat it. He sent it back. They gave us credi. The fish tacos were\n  just okay nothing impressive about their food at all.", "negative"), Example("I\n  did not get to see the beach when I tried on a Saturday when driving from\n  ragged point to Monterey bay. I was turned back because the park is full but\n  this review is about how difficult and perhaps dangerous entering the park\n  from HW1. First it is a very sharp turn with no easy way to see any car\n  coming out when you turn into the park entrance. Second it is a steep decline\n  going down after the turn. So for someone not familiar with driving on a\n  slope, this is not a comfortable place to visit. Getting out is almost as bad\n  if multiple cars got trapped on the way up the slope. And why the CA rangers\n  cannot set up a lot full sign before cars getting down the slope from HW1 is\n  beyond me? They may think it is fun going up and down the slope.", "negative"), Example("Used\n  to be the most amazing beach but Illinois and Indiana people have overrun and\n  ruined it. Litter everywhere. People have room but decide to sit right next\n  to you up your ___. People let their dogs run free and one went right up to\n  the water where I was swimming and pissed into the water. Campsite prices\n  have doubled and it\'s near impossible to even find an opening anymore. Can\'t\n  even rent any of the huts. They get fully booked up a year in advance. Very\n  sad. I miss you old Weko!", "negative"), Example("Too long a\n  distance from street/boardwalk to water. It\'s nice that it\'s free though, so\n  I\'m giving it 4 stars for that reason.", "neutral"), Example("If you\n  park near the convention center and walk that boardwalk out, there are two\n  showers and a set of bathrooms. There is a surf shack! You can buy relatively\n  normal priced food and you can rent surfboards. You can also get a surf\n  lesson!", "neutral"), Example("I know\n  this is against the grain from mostly all reviews but this beach was not what\n  I expected.There was trash everywhere we went on this beach including in the\n  water and in the tidal pools. In fact, there was broken glass in some of the\n  tidal pools! The beach was so crowded even on a week day with most of the\n  kids back at school. We could not even see the water from our chairs because\n  it was so so crowded and people were right on top of one another with barely\n  anywhere to walk between people\'s set ups to get to the water. We had to walk\n  way down to the end of the beach to get some space and photos without crowds\n  in the background. That area was much nicer but too long of a walk for us to\n  take our chairs and things down there. The water was super crowded and had an\n  oily residue on top of it. We were lucky we didn\'t have traffic or parking\n  issues like so many others mentioned. I didn\'t think it was worth the 2 hour\n  drive for us.", "neutral"), Example("Town Beach\n  open to the public for modest admission. Nice location on Lake Michigan;\n  includes sit-down eatery. Good beach destination from Chicago", "neutral"),
        Example("The beach\n  is gorgeous: incredible white powdery sand, nice landscaping with low\n  buildings and miles and miles of beaches to enjoy (when that\'s possible). We\n  visited this beach from October 6th to October 8th (when we had to leave due\n  to Hurricane Michael) and red tide was horrible. You could only stay at the\n  beach (or near it) very early in the morning to avoid coughing; then, when\n  the wind direction changed, it all started again: cough, runny nose, scratchy\n  throats and hundreds of dead fish on the sand: what a terrible pity!!! A\n  pity, yes, for visitors, for the fauna, for locals!!!! I know red tide is\n  supposed to be a natural phenomenon, but is it really so??? Can\'t there be\n  some other human-made factor boosting it??? I talked to a man who owns a house\n  on the beach, and he said he had never seen such a terrible red tide in the\n  twenty years he\'s owned his house. So...I believe it\'s time for everybody to\n  think what kind of planet we want to live in, and act in consequence, or we\n  run the risk of seeing this kind of event (and many others)more often!! To\n  sum up, Santa Rosa Beach is an awesome beach, which we couldn\'t enjoy due to\n  red tide! (Of course, no swimming at all!)", "neutral")])

    ## enablePrint()  

    # print('The confidence levels of the labels are: {}'.format(
    #        classifications.classifications))

    example=list(classifications.classifications)
    predcitions=[exmpl.prediction for exmpl in example]

    return predcitions,sentiments
