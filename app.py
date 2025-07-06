import tkinter as tk
from tkinter import ttk
import time
import csv
import os

PROMPTS = [
    "Pope Leo XIII",
    "Donald Trump",
    "Stephen Hawking",
    "Fishing Story",
    "Frost Poem",
    "Israel News",
    "Future of AI",
    "Henry Adams Essay",
    "Mansfield Park Essay",
    "Liberal Arts Extract",
]

PROMPT_TEXTS = [
    """Setting. Following the Industrial Revolution, liberalism, capitalism, and socialism competed for allegiance in nineteenth-century Europe and America. European Catholic leaders were discussing economic problems and the harsh plight of industrial workers. In 1890, Emperor William II convened an international conference in Berlin on problems of labor. Unions were developing in a conflicted industrial arena. In the United States, a majority of bishops supported the Knights of Labor, narrowly averting a papal condemnation of the Knights in the late 1880s based on issues around membership by workers of all faiths and no faith.
        Pope Leo XIII commissioned and carefully reviewed a first draft by the Jesuit Matteo Liberatore, then another by the Dominican Cardinal Tommaso Maria Zigliara, then a third version involving Liberatore with the Jesuit Cardinal Camillo Mazzella, revised yet again by Msgr. Gabriele Boccali, one of the pope’s secretaries.
        Summary. Pope Leo examined the misery and exploitation of industrial workers and families, noting the destitution of many and the concentration of wealth by few. Rejecting class warfare and denial of property rights, Leo affirmed private possession and the common purpose of property, distinguishing just ownership from just use. He taught the duty to pay a living wage, rights to organize, and collaboration rather than class struggle. Leo sets the framework for the next century: opposing liberalism, which deifies reason, freedom, and conscience, but also opposing socialism, which gives too great a role to the state and does not recognize individual dignity and rights.
        The church has a right to speak out on social issues and promote social reconciliation. The state in turn must intervene when the common good or a particular class suffers and there is no other remedy. The state should protect property rights for as many as possible and rights of association and religion, as well as assuring that workers are paid sufficiently to be adequately housed, clothed and bodily fit.
        Key Ideas Moral Outrage. By declaring that some opportune remedy must be found quickly for the misery and wretchedness pressing so unjustly on the majority of the working class, Pope Leo set the Church firmly amid the burning social questions of his day. He denounced a rapacious usury and concentration of economic power so that a small number of very rich men have been able to lay upon the teeming masses of the laboring poor a yoke little better than that of slavery itself. Beyond the content, Leo laid a solid foundation for later social teachings: perhaps even more important was the character of the document as a cry of protest against the exploitation of poor workers.
        His intervention was a solemn rejection of a dominant economic tenet of the day, that labour is a commodity to be bought at market prices determined by the law of supply and demand rather than by the human needs of the worker. Leo’s was a stinging protest against the economic status quo, and its effect over time was to move social issues to the center of the Church’s mission, driving home the idea that Catholics must have a social conscience, and to encourage those already so committed.
        Workers’ Rights and Duties. Working from a framework of natural law, Pope Leo built upon the foundational concept of human dignity and the related belief that work is not just a commodity. From these he developed specific worker rights: freedom to receive and spend wages as they see fit; integrity of family life, including providing necessities to children; wages sufficient to support a worker who is frugal and well-behaved and, by implication, his or her family. This concept of a family wage will be clarified and grow across the 130-year tradition, but it is rooted here in Pope Leo’s writing.
    """,
    """Donald Trump was first elected on November 8, 2016, in what was widely seen as a surprise upset victory. He was inaugurated as the 45th President of the United States on January 20, 2017. By the time he left office after losing the 2020 presidential election to former Vice President Joe Biden, Trump’s first term was largely defined by scandal, investigation, and intense partisan division. Both supporters and critics often used the word “unprecedented” to describe his time in office. The historically unusual nature of his presidency was confirmed four years later when he became the second person ever, and the first since the 19th century, elected to two non-consecutive terms. He took the oath of office for the second time on January 20, 2025.
        A number of factors marked Trump as distinctive even before his time in the White House began. At 70 years old in 2016, he became the oldest person to ever assume the presidency, surpassing a record set by Ronald Reagan, who was 69 when he took office in 1981. Trump’s successor, Joseph Biden, re-set the record for oldest president when he was inaugurated four years later, shortly after his 78th birthday. Trump again became the oldest president to be inaugurated on January 20, 2025, at the age of 78 and a half.
        He was also the first president never to have served in either public office or in military leadership before arriving in the White House. Finally, in 2016, he became the fifth person (and the second in sixteen years) to win a victory in the Electoral College but to lose the popular vote. His Democratic challenger in 2016, Hillary Clinton, won 2.8 million more votes than Trump did, but he prevailed in the Electoral College, 304 to 227. In 2024, Trump defeated Vice President Kamala Harris in both the Electoral College, 312 to 226, and the popular vote, 49.9 percent to 48.4 percent.
        Trump was also the first US president to be impeached twice. In December 2019, the Democratically controlled House of Representatives impeached President Trump on the charge of abuse of power and obstruction of Congress because of his efforts to persuade a foreign leader, President Volodymyr Zelensky of Ukraine, to interfere with the upcoming US presidential election. He stood trial in the Senate and was acquitted in February 2020.
        The House of Representatives impeached President Trump again in January 2021. In a stark break from all past precedent, Trump refused to concede the 2020 presidential election or acknowledge the legitimacy of Biden’s victory, in which Biden won approximately 7 million more votes and the Electoral College vote by 306 to 232. Trump led a protracted effort to undermine the certification of the votes, which culminated when his supporters violently assaulted the US Capitol on January 6, 2021. That event led to a second impeachment. Trump stood trial in the Senate and was acquitted again several weeks after his term expired.
    """,
    """Friends and colleagues from the University of Cambridge have paid tribute to Professor Stephen Hawking, who died today at the age of 76.
        Widely regarded as one of the world’s most brilliant minds, he was known throughout the world for his contributions to science, his books, his television appearances, his lectures and through biographical films. He leaves three children and three grandchildren.
        Professor Hawking broke new ground on the basic laws which govern the universe, including the revelation that black holes have a temperature and produce radiation, now known as Hawking radiation. At the same time, he also sought to explain many of these complex scientific ideas to a wider audience through popular books, most notably his bestseller A Brief History of Time.
        He was awarded the CBE in 1982, was made a Companion of Honour in 1989, and was awarded the US Presidential Medal of Freedom in 2009. He was the recipient of numerous awards, medals and prizes, including the Copley Medal of the Royal Society, the Albert Einstein Award, the Gold Medal of the Royal Astronomical Society, the Fundamental Physics Prize, and the BBVA Foundation Frontiers of Knowledge Award for Basic Sciences. He was a Fellow of The Royal Society, a Member of the Pontifical Academy of Sciences, and a Member of the US National Academy of Sciences.
        He achieved all this despite a decades-long battle with motor neurone disease, with which he was diagnosed while a student, and eventually led to him being confined to a wheelchair and to communicating via his instantly recognisable computerised voice. His determination in battling with his condition made him a champion for those with a disability around the world.
        Professor Hawking came to Cambridge in 1962 as a PhD student, and rose to become the Lucasian Professor of Mathematics, a position once held by Isaac Newton, in 1979. In 2009, he retired from this position and was the Dennis Stanton Avery and Sally Tsui Wong-Avery Director of Research in the Department of Applied Mathematics and Theoretical Physics until his death. He was also a member of the University's  Centre for Theoretical Cosmology, which he founded in 2007. He was active scientifically and in the media until the end of his life.
    """,
    """CHAPTER I\nA FISHING VILLAGE\nOF the tens of thousands of excursionists who every summer travel down by rail to Southend, there are few indeed who stop at Leigh, or who, once at Southend, take the trouble to walk three miles along the shore to the fishing village. It may be doubted, indeed, whether along the whole stretch of coastline from Plymouth to Yarmouth there is a village that has been so completely overlooked by the world. Other places, without a tithe of its beauty of position, or the attraction afforded by its unrivalled view over the Thames, from Gravesend to Warden Point, ever alive with ships passing up and down, have grown from fishing hamlets to fashionable watering-places; while Leigh remains, or at any rate remained at the time this story opens, ten years ago, as unchanged and unaltered as if, instead of being but an hour's run from London, it lay far north in Scotland.\nIts hill rises steeply behind it; there is room only for the street between the railway and the wharves, and for a single row of houses between the line and the foot of the hill. To get into Leigh from the country round it is necessary to descend by a steep road that winds down from the church at the top of the hill; to get out again you must go by the same way. The population is composed solely of fishermen, their families, and the shopkeepers who supply their necessities. The men who stand in groups in the street and on the wharf are all clad in blue guernseys or duck smocks and trousers of pilot cloth or canvas. Broad-built sturdy men are they, for in point of physique there are few fishermen round the coast who can compare with those of Leigh.\nA stranger in the place would think that the male population had nothing to do but to stand in the street and talk, but night is for the most part their time for work; although many of the bawleys go out on the day-tide also, for at Leigh the tide is all-important. For five hours in the day it washes the foot of the wharves, for seven a wide expanse of mud stretches away to Canvey Island in front, and Southend Pier to the east.\nAt the wells--for Leigh still depends for water on its wells--are, during the hours at which water is permitted to be drawn, lines of twenty women and girls with pails, each patiently waiting her turn. There are not many boys about, for boys require more sleep than men, and a considerable portion of their time on shore is spent in bed.
    """,
    """The line-storm clouds fly tattered and swift, the road is forlorn all day, where a myriad snowy quartz stones lift, and the hoof-prints vanish away. The roadside flowers, too wet for the bee, expend their bloom in vain. Come over the hills and far with me, and be my love in the rain. The birds have less to say for themselves in the wood-world’s torn despair than now these numberless years the elves, although they are no less there: all song of the woods is crushed like some wild, easily shattered rose. Come, be my love in the wet woods; come, where the boughs rain when it blows. There is the gale to urge behind and bruit our singing down, and the shallow waters aflutter with wind from which to gather your gown. What matter if we go clear to the west, and come not through dry-shod? For wilding brooch shall wet your breast the rain-fresh goldenrod. Oh, never this whelming east wind swells but it seems like the sea’s return to the ancient lands where it left the shells before the age of the fern; and it seems like the time when after doubt our love came back amain. Oh, come forth into the storm and rout and be my love in the rain.
    """,
    """“There are no free wars,” Prime Minister Benjamin Netanyahu warned Israelis on Friday, and Iran has landed a few missiles out of the many it fired at Israeli cities. But a series of mistakes has led Iran to the catastrophic scenario it has long sought to avoid: open war with Israel without the aid of proxies and before obtaining nuclear weapons. How did Tehran miscalculate so badly? For months President Trump made clear that he wanted to avoid a military confrontation and make a nuclear deal. He all but begged the regime to come to terms, and his envoy Steve Witkoff made a generous offer—too generous—that would have let Iran continue enriching uranium domestically for some years. Ayatollah Ali Khamenei dismissed it out of hand. “Who are you to decide whether Iran should have enrichment?” he asked. The Iranians evidently thought they would pay no price for blowing past the President’s 60-day ultimatum and his red line on nuclear enrichment. So long as they kept talking, they presumed they could string along Mr. Trump, who would shield them from Israel. Did they think Tucker Carlson called the shots and the U.S. would roll over each time it was pushed? On deadline day Iran said it would begin enrichment at a secret site, another Nuclear Non-Proliferation Treaty violation. Tehran underestimated Mr. Trump, who knew Israel’s plan but declined to expose or block it. Democrats now criticize him for that, and a different President may well have prevented Israel’s campaign to eliminate the Iranian sword of Damocles that looms over its head and ours. Instead Mr. Trump kept a flexible enough posture to embrace the attack after its early success.
    """,
    """The effects of this machine renaissance have permeated society: voice recognition devices such as Alexa, recommendation engines like those used by Netflix to suggest which movie you should watch next based on your viewing history, and the modest steps taken by driverless cars and other autonomous vehicles are emblematic of a rudimentary stage of 21st century AI. ChatGPT 4, Dall-E, Midjourney and other contemporary generative AI systems are currently disrupting most business sectors. But the next five years of AI development will likely lead to major societal changes that go well beyond what we've seen to date.\nHow will AI impact the future? The most obvious change that many people will feel across society is an increase in the tempo of engagements with large institutions. Any organization that engages regularly with large numbers of users—businesses, government units, nonprofits—will be compelled to implement AI in the decision-making processes and in their public- and consumer-facing activities. AI will allow these organizations to make most of the decisions much more quickly. As a result, we will all feel life speeding up.
        \nBusiness enterprises will almost certainly be compelled to integrate and exploit generative AI to improve efficacy, profitability and, most immediately, efficiency. Corporations’ duty to increase shareholder value and fear of falling behind competitors that integrate and deploy AI more aggressively will make for a virtually irresistible imperative: fully embrace AI or see your investors turn bearish as peers pull ahead.
        \nSociety will also see its ethical commitments tested by powerful AI systems, especially privacy. AI systems will likely become much more knowledgeable about each of us than we are about ourselves. Our commitment to protecting privacy has already been severely tested by emerging technologies over the last 50 years. As the cost of peering deeply into our personal data drops and more powerful algorithms capable of assessing massive amounts of data become more widespread, we will probably find that it was a technological barrier more than an ethical commitment that led society to enshrine privacy.
    """,
    """	Henry Adams loathes the modern loss of understanding about the essence of reality that somehow has accompanied and grown with brilliant technological innovation. It seems that the more brilliantly we light our cities during world fairs, the less we feel the need to look to the sun for light and the less light shines in our minds. Somehow, on the one hand man builds bigger and more sophisticated things, on the other the less man respects himself. Modern scientists hold the flattering view that we humans are best described as random quantum clouds among quantum clouds in a universe of quantum clouds. We have no place in this universe other than what we wrench away by force, nothing has a nature, and there is no Creator bringing order. Adams rejects this literally disintegrated outlook on reality in favor of the Catholic Medieval understanding among whose fruits are Mount St. Michelle and Chartres Cathedral In the Medieval world, everything had a place and purpose, and because of the higher order of reality, everything was beautifully symbolic as well. Mount St. Michelle was not only a fort built by human ingenuity but it also looks beautiful and draws the mind to the great strength and unassailable reason of Saint Michael. St. Michael, too, played a quite practical role in defending mankind from the devil! Chartres cathedral, on the other hand, is not only a practical place of worship whose men can literally receive forgiveness form all their sins (the question of justice drove the pagans absolutely mad) but the structure is also a careful image of the feminine in the universe and of the great Virgin Mary whose beauty lay not in anything she did of her own greatness (otherwise the cathedral was better a factory) but in her acceptance of God’s plan and grace for her (hence Chartres’ stained glass windows are nothing by themselves but the most beautiful masterpieces who the sun shines through in a million hues). The medievals had an integrated view of a loving Creator who gifted an awesome universe to his people, and then, when they rejected him, gave them the Church as a practical and concrete way of rising above their sin and becoming like God.
    """,
    """In Mansfield Park Jane Austin presents one of her most controversial heroines - Fanny Price. Fanny first appears as a shy, needy girl constantly “finding something to fear in every person and place” whose dependent situation and inability to insist on her own way nearly lowers her to the level of a servant (II). Austin tempts the reader to become exasperated with Fanny, dangling scene after scene before the reader’s eyes of Fanny’s constant agitation combined with her frustrating refusal to speak up for herself. About the time of Fanny’s coming of age, when most of her family has earmarked her as a timid servant girl to be bossed around, Fanny abruptly turns that notion on its head by heatedly refusing to act in a risqué play that her cousins put on. Strengthened in her principles by having to disrupt the plans of her cousins and brave the storm of their annoyance, Fanny is prepared for the much harder task of denying the coveted advances of Henry Crawford, whom she knows to be duplicitous, against the wishes of all her family and friends. When Crawford fornicates with Maria and Julia elopes with Yates, Fanny alone in the Bertram household emerges as a moral compass, a rock that refuses to be washed away by the tides of popular sentiment.\nWhen Fanny Price first comes to Mansfield, her naturally timid disposition is only heightened by the subordinate position she is placed in, and her completely passive attitude does not strike the reader as virtuous but rather indicative of a terror at displeasing her relatives and benefactors. During the first week at her new home, Fanny, whether near or from her cousins, whether in the schoolroom, the drawing-room, or the shrubbery, was equally forlorn, finding something to fear in every person and place…The rooms were too large for her to move in with ease: whatever she touched she expected to injure, and she crept about in constant terror of something or other; often retreating towards her own chamber to cry” (II)\nIn fact, until her cousin Edmund becomes her intercessor and demands attention be given to Fanny, Fanny does not even have the courage to ask for pen and paper to write a letter to her brother William. This fearfulness does not originate from the novelty of living with her wealthy cousins, however - the reader learns that even in the home she grew up in Fanny relies on William who is “her advocate with her mother (of whom he was the darling) in every distress” (II). Fanny is simply a timid soul by nature who desperately wants to please. Strangely, as she grows more familiar with the Bertram household and develops the habit of constantly jumping up and doing odd jobs for her cousins, her acts of service leave an odd taste in the mouth of the reader. Add this to the fact that she is introduced into the Bertram household as a hybrid between a houseguest and a handmaid, and there is reasonable cause to suspect her of being obsequious rather than uncommonly generous. To prove herself genuinely virtuous and separate herself from those timid souls blown about by desire for others’ good opinion, Fanny must be placed in and overcome a situation where she cannot both do the right thing and please.
    """,
    """A common misconception about the liberal arts education is that it only focuses on grand ideas and lofty thoughts without grounding students in the real world and letting them experience things firsthand. UD’s Rome program certainly puts to silence any such claims because not only do UD students get to visit the birthplaces of the Church and Western Civilization and all the old, serene cities where the ideas we learn now were formulated, but we get to actually live for an entire semester among the very things and places we are studying! An experience like that is absolutely unparalleled and has massive potential to enrich a student’s life and round out their education into perfection.\nTo begin with, beauty is simply good for the human soul. As a famous author once wrote, “beauty will save the world.” (Incidentally, that author’s country is both uniquely bereft of beauty and not doing well). Beauty refreshes the mind and shows us how good the universe is that God has made for us. Being in a truly beautiful place awes the mind and, quite frankly, inspires us to live better. That is why the UD Rome experience is so brilliant, because it allows students to experience firsthand the most beautiful art and nature in the entire world! Nowhere are there more majestic mountains, bluer lakes, or more vibrant landscapes than in Europe. Nowhere but Italy can a student stroll out the door and encounter on every street corner gigantic cathedrals huge enough to dwarf the Olympians’ temples, but so intricately carved and carefully painted that even the locals can never know even half their beauty! In addition, the terrific external beauty of the Catholic cathedrals in Rome is not only good in itself, but, more importantly, is a reflection of the awesome beauty of the Church, and the ability to see the beauty of the Church where it was founded is a great gift to us UD students. \nOn top of the beauty that surrounds UD students in Rome, the Rome semester rounds out the classical education that UD offers. Studying the contribution of Socrates, Aristotle, and Plato to Western Civilization and the Catholic philosophical tradition is enlightening enough when done through books, but the student never gets closer to leaving the cave and looking reality in its face when in the birthplace of Western Civilization and the Catholic Church. The Rome semester offers the opportunity for a student to read Aquinas and then visit where he lived and wrote. This semester connects the body and mind in a way that is sorely lacking in our culture especially today; communication is so effortless that we try to disconnect our minds from the physical world like angels. However, since we aren’t angels, we need to be in the physical presence of people and beautiful things that we are talking with or about to really understand them. Being in the same places where the great thinkers strolled, the legendary theologians wrote and prayed, and God himself died to atone for our sins gives us a far deeper insight into our Western heritage than only talking or reading about these things ever could.
    """
]

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Biometric Logger")

        self.keystrokes = []
        self.key_down_times = {}
        self.session_start = time.time()

        self.build_ui()
        self.setup_resizing()

    def build_ui(self):
        # Username input
        tk.Label(self.root, text="Username:").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, columnspan=2, sticky="ew")

        # Prompt selector
        tk.Label(self.root, text="Select Prompt:").grid(row=1, column=0, sticky="w")
        self.prompt_var = tk.StringVar()
        self.prompt_dropdown = ttk.Combobox(self.root, textvariable=self.prompt_var, values=PROMPTS, state="readonly")
        self.prompt_dropdown.grid(row=1, column=1, columnspan=2, sticky="ew")
        self.prompt_dropdown.bind("<<ComboboxSelected>>", self.load_prompt)

        # Prompt text area (background matched to typing area)
        self.prompt_text = tk.Text(self.root, height=10, wrap="word", bg="white", fg='black')
        self.prompt_text.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.prompt_text.insert("1.0", "Choose a prompt from the dropdown.")
        self.prompt_text.config(state="disabled")

        # Typing area
        tk.Label(self.root, text="Type here:").grid(row=3, column=0, sticky="w")
        self.typing_area = tk.Text(
            self.root, 
            height=10, 
            wrap="word", 
            bg="white", 
            fg="black", 
            insertbackground="black",
        )
        self.typing_area.grid(row=4, column=0, columnspan=3, sticky="nsew")
        self.typing_area.bind("<KeyPress>", self.on_key_down)
        self.typing_area.bind("<KeyRelease>", self.on_key_up)
        

        # Save button
        self.save_button = tk.Button(self.root, text="Save Keystrokes", command=self.save_keystrokes)
        self.save_button.grid(row=5, column=1, pady=10)

        # Notification label
        self.notification = tk.Label(self.root, text="", fg="green")
        self.notification.grid(row=6, column=0, columnspan=3)

    def setup_resizing(self):
        for i in range(3):
            self.root.columnconfigure(i, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(4, weight=2)

    def load_prompt(self, event=None):
        prompt = self.prompt_var.get()
        prompt_index = PROMPTS.index(prompt)
        text = PROMPT_TEXTS[prompt_index]
        self.prompt_text.config(state="normal")
        self.prompt_text.delete("1.0", tk.END)
        self.prompt_text.insert("1.0", text)
        self.prompt_text.config(state="disabled")
        self.typing_area.delete("1.0", tk.END)
        self.keystrokes.clear()
        self.key_down_times.clear()
        self.session_start = time.time()
        self.notification.config(text="")

    def on_key_down(self, event):
        key = event.keysym
        now = time.time()
        if key not in self.key_down_times:
            self.key_down_times[key] = now

    def on_key_up(self, event):
        key = event.keysym
        now = time.time()
        down_time = self.key_down_times.pop(key, None)

        if down_time:
            self.keystrokes.append({
                'key': key,
                'keydown_time': round((down_time - self.session_start) * 1000, 3),
                'keyup_time': round((now - self.session_start) * 1000, 3),
                'hold_time': round((now - down_time) * 1000, 3)
            })

    def save_keystrokes(self):
        username = self.username_entry.get().strip()
        if not username:
            self.notification.config(text="Username is required", fg="red")
            return

        os.makedirs("logs", exist_ok=True)
        filename = f"logs/{username}_{int(time.time())}.csv"

        with open(filename, "w", newline='') as f:
            for row in self.keystrokes:
                row['participant'] = username
            writer = csv.DictWriter(f, fieldnames=["participant", "key", "keydown_time", "keyup_time", "hold_time"])
            writer.writeheader()
            writer.writerows(self.keystrokes)
            

        self.notification.config(text=f"Saved to {filename}", fg="green")
        self.keystrokes.clear()
        self.key_down_times.clear()
        self.session_start = time.time()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
