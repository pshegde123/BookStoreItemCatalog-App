from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a dummy user
user1 = User(name="user1", email="dummyuser1@gmail.com")
session.add(user1)
session.commit()

user2 = User(name="Pradnya Hegde", email="pradnyahegde@gmail.com")
session.add(user2)
session.commit()


# Book store catalog
Fiction = Catalog(name="Fiction")
session.add(Fiction)
session.commit()

item11 = Item(
    name="Life of Pi",
    description="\
Synopsis:Life of Pi is a fantasy adventure novel by \
Yann Martel published in 2001. \
The protagonist is Piscine Molitor Pi  Patel, \
an Indian boy from Pondicherry who explores issues of spirituality \
and practicality from an early age. \
He survives 227 days after a shipwreck while stranded on a lifeboat in \
the Pacific Ocean with a Bengal tiger named Richard Parker.",
    catalog=Fiction,
    user=user1)
session.add(item11)
session.commit()

item12 = Item(
    name="Wuthering Heights",
    description="Wuthering Heights is Emily Bronte's first and only published \
    novel, written between October 1845 and June 1846, and published in 1847 \
    under the pseudonym Ellis Bell; Bronte died the following year, aged 30. \
    The decision to publish came after the success of her sister Charlotte's \
    novel, Jane Eyre. After Emily's death, Charlotte edited the manuscript of \
    Wuthering Heights, and arranged for the edited version to be published as \
    a posthumous second edition in 1850. Wuthering Heights is the name of the \
    farmhouse where the story unfolds. The book's core theme is the \
    destructive effect of jealousy and vengefulness both on the jealous or \
    vengeful individuals and on their communities.",
    catalog=Fiction,
    user=user2)
session.add(item12)
session.commit()

item13 = Item(
    name="Great Expectations",
    description="Great Expectations is the thirteenth novel by Charles \
    Dickens \
    and his penultimate completed novel: a bildungsroman that depicts the \
    personal growth and personal development of an orphan nicknamed Pip. \
    It is Dickens's second novel, after David Copperfield, to be fully \
    narrated in the first person.[N 1] The novel was first published as a \
    serial in Dickens's weekly periodical All the Year Round, from 1 December \
    1860 to August 1861.[1] In October 1861, Chapman and Hall published the \
    novel in three volumes.[2]",
    catalog=Fiction,
    user=user1)
session.add(item13)
session.commit()

item14 = Item(
    name="The Wonderful Wizard of OZ",
    description="Dorothy is a young girl who lives on a Kansas farm with \
    her Uncle Henry, Aunt Em, and little dog Toto. One day the farmhouse, \
    with Dorothy inside, is caught up in a tornado and deposited in a field \
    in the country of the Munchkins. The falling house kills the Wicked Witch \
    of the East.",
    catalog=Fiction,
    user=user2)
session.add(item14)
session.commit()

Teens = Catalog(name="Teens")
session.add(Teens)
session.commit()

item21 = Item(
    name="The fault in our stars",
    description="Despite the tumor-shrinking medical miracle that has bought \
    her a few years, Hazel has never been anything but terminal, her final \
    chapter inscribed upon diagnosis. But when a gorgeous plot twist named \
    Augustus Waters suddenly appears at Cancer Kid Support Group, \
    Hazel's story is about to be completely rewritten.",
    catalog=Teens,
    user=user2)
session.add(item21)
session.commit()

item22 = Item(
    name="Wonder",
    description="Born with a facial anomaly that has required over two-dozen \
    surgeries,\
10-year-old Auggie Pullman is a pretty ordinary, Xbox-playing, ice \
cream-loving kid behind the face.\
When he gets to attend elementary school after a lifetime of home \
schooling, he's excited and scared.\
Even with the support of his close-knit, loving family, being the new kid \
is always rough,\
but with a face that often elicits both stares and shrieks, it's even \
harder.\
Auggie starts Beecher Prep and discovers who is a real friend and who \
isn't, and the challenges of community.\
With multiple narrators, observations of Auggie and \
his experience are diverse, adding nuance and depth to the story.",
    catalog=Teens,
    user=user1)
session.add(item22)
session.commit()

Childrens = Catalog(name="Kids")
session.add(Childrens)
session.commit()

item31 = Item(
    name="Diary of a Wimpy Kid #1",
    description="In book one of this debut series, Greg is happy to have \
    Rowley, his sidekick, along for the ride. But when Rowleys star starts \
    to rise, Greg tries to use his best friends newfound popularity to his \
    own advantage, kicking off a chain of events that will test their \
    friendship in hilarious fashion.",
    catalog=Childrens,
    user=user1)
session.add(item31)
session.commit()

item32 = Item(
    name="Diary of a Wimpy Kid #2",
    description="The highly anticipated sequel to the #1 \
    NEW YORK TIMES bestselling book! ",
    catalog=Childrens,
    user=user2)
session.add(item32)
session.commit()

item33 = Item(
    name="Bedtime Stories for Kids",
    description="This is an excellent read for beginning and early readers. \
    Each story is easy to read and exciting. Cute and bright illustrations \
    for younger readers!",
    catalog=Childrens,
    user=user1
)
session.add(item33)
session.commit()

item34 = Item(
    name="Peter Pan",
    description="Peter Pan, the book based on J.M. Barrie's famous play, is \
    filled with unforgettable characters: Peter Pan, the boy who would not \
    grow up; the fairy, Tinker Bell; the evil pirate, Captain Hook; and the \
    three children--Wendy, John, and Michael--who fly off with Peter Pan to \
    Neverland, where they meet Indians and pirates and a crocodile that ticks",
    catalog=Childrens,
    user=user2
)
session.add(item33)
session.commit()

Comics = Catalog(name="Comics")
session.add(Comics)
session.commit()

item41 = Item(
    name="Justice League",
    description="In a world where inexperienced superheroes operate under a \
    cloud of suspicion from the public, loner vigilante Batman has stumbled \
    upon a dark evil that threatens to destroy the earth as we know it. Now, \
    faced with a threat far beyond anything he can handle on his own, the \
    Dark Knight must trust an alien, a scarlet speedster, an accidental \
    teenage hero, a space cop, an Amazon Princess and an undersea monarch. \
    Will this combination of Superman, The Flash, Cyborg, Green Lantern, \
    Wonder Woman and Aquaman be able to put aside their differences and come \
    together to save the world? Or will they destroy each other first?",
    catalog=Comics,
    user=user2)
session.add(item41)
session.commit()

item42 = Item(
    name="The Flash",
    description="Struck by a bolt of lightning and doused in chemicals, \
    Central City Police scientist Barry Allen was transformed into the \
    fastest man alive. Tapping into the energy field called The Speed Force, \
    he applies a tenacious sense of justice to protect an serve the world as \
    The Flash!",
    catalog=Comics,
    user=user1)
session.add(item42)
session.commit()

item43 = Item(
    name="Teen Titans",
    description="Tim Drake, Batman's former sidekick, is back in action when \
    an international organization called Project N.O.W.H.E.R.E. seeks to \
    capture, kill or co-opt super-powered teenagers. As Red Robin, he's going \
    to have to team up with the mysterious and belligerent powerhouse thief \
    known as Wonder Girl, the hyperactive speedster calling himself Kid Flash \
    and few more all-new teen super-heroes to stand any chance at all against \
    N.O.W.H.E.R.E. But as Superboy meets them for the first time, the Titans \
    have to wonder, is he a friend - or foe?",
    catalog=Comics,
    user=user1)
session.add(item42)
session.commit()


Graphic = Catalog(name="Graphic Novels")
session.add(Graphic)
session.commit()

item51 = Item(
    name="The Wonderful Wizard of Oz (Graphic Novel)",
    description="The premier American fantasy adventure gets the Merry Marvel \
    treatment! Eisner Award-winning writer/artist Eric Shanower teams up with \
    fan-favorite artist Skottie Young (New X-Men) to bring L. Frank Baum's \
    beloved classic to life! When Kansas farm girl Dorothy flies away to the \
    magical Land of Oz, she fatally flattens a Wicket Witch, liberates a \
    Scarecrow and is hailed by the Munchkin people as a great sorceress...\
    but all she really wants to know is: how does she get home?",
    catalog=Graphic,
    user=user1)
session.add(item51)
session.commit()

item52 = Item(
    name="The Hobbit: Graphic Novel",
    description="The Hobbit is the story of Bilbo Baggins,a quiet and \
    contented hobbit whose life is turned upside down when he joins the \
    wizard Gandalf and thirteen dwarves on their quest to reclaim the \
    dwarves stolen treasure. It is a journey fraught with danger and in the \
    end it is Bilbo alone who must face the guardian of this treasure, the \
    most-dreaded dragon Smaug.\
    Illustrated in full colour throughout, and accompanied by the carefully \
    abridged text of the original novel, this handsome authorised edition \
    will introduce new generations to a magical masterpiece and be \
    treasured by Hobbit fans of all ages, everywhere. ",
    catalog=Graphic,
    user=user1)
session.add(item52)
session.commit()

Magazine = Catalog(name="Magazines")
session.add(Magazine)
session.commit()

item61 = Item(
    name="National Geographics",
    description="National Geographic is the official magazine of the National \
    Geographic Society. It has been published continuously since its first \
    issue in 1888, nine months after the Society itself was founded. It \
    primarily contains articles about science, geography, history, and \
    world culture.",
    catalog=Magazine,
    user=user1)
session.add(item61)
session.commit()

item62 = Item(
    name="Nature",
    description="Nature is a British multidisciplinary scientific journal, \
    first published on 4 November 1869. It was ranked the world's most cited \
    scientific journal by the Science Edition of the 2010 Journal Citation \
    Reports and is ascribed an impact factor of 40.137, making it one of the \
    world's top academic journals.[2][3] It is one of the few remaining \
    academic journals that publishes original research across a wide range \
    of scientific fields.",
    catalog=Magazine,
    user=user1)
session.add(item62)
session.commit()

item63 = Item(
    name="The Atlantic",
    description="The Atlantic is an American magazine and multi-platform \
    publisher.It was founded in 1857 as The Atlantic Monthly in Boston, \
    Massachusetts, and began as a literary and cultural commentary magazine \
    publishing leading writers' commentary on abolition, education, and other \
    major issues in contemporary political affairs.",
    catalog=Magazine,
    user=user2)
session.add(item63)
session.commit()

print "added catalog items"
