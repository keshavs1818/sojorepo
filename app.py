from datetime import date, timedelta

import streamlit as st


st.set_page_config(page_title="Math Quest Studio", page_icon="+", layout="wide")

WEEK_TAB_NAMES = [
    "Decode the Date",
    "More to Explore",
    "What's Left?",
    "Operation Sleuths",
    "Group Groove",
    "Zero Has a Job",
    "Add It or Group It?",
    "Fair Share Crew",
    "Choose Your Move",
    "Four-Way Math Match",
    "Calendar Countdown",
    "Math Mission Finale",
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --ink:#1d2939; --muted:#667085; --mint:#dff5e9; --coral:#f47c6c; --gold:#f5c563; }
    html, body, [class*="css"] { font-family:'DM Sans',sans-serif; color:var(--ink); }
    .stApp { background:radial-gradient(circle at 85% 5%,#fce6c8 0,transparent 25%),linear-gradient(135deg,#fffdf8 0%,#f5f8f4 100%); }
    h1,h2,h3 { font-family:'Space Grotesk',sans-serif; letter-spacing:0; }
    h1 { font-size:clamp(2.2rem,5vw,4.4rem); line-height:.98; }
    .hero { padding:2.4rem 0 1.4rem; max-width:850px; }
    .eyebrow { color:#c45443; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
    .hero p { color:var(--muted); font-size:1.05rem; max-width:690px; }
    .lesson-card,.tip-card { background:rgba(255,255,255,.78); border:1px solid #e4e7df; border-radius:8px; padding:1.1rem 1.25rem; height:100%; }
    .lesson-card strong { font-family:'Space Grotesk',sans-serif; font-size:1.15rem; }
    .number { display:inline-flex; align-items:center; justify-content:center; width:2rem; height:2rem; border-radius:50%; background:var(--coral); color:white; font-weight:700; margin-bottom:.65rem; }
    .prompt { background:#182b3a; color:white; border-radius:8px; padding:1.3rem 1.4rem; margin:1rem 0; }
    .prompt small { color:#b8d8df; text-transform:uppercase; letter-spacing:.1em; font-weight:700; }
    .date-example { background:var(--gold); border-radius:8px; padding:1rem; font-family:'Space Grotesk',sans-serif; font-size:1.5rem; text-align:center; }
    .answer { background:var(--mint); border-left:5px solid #4caa79; padding:.8rem 1rem; border-radius:4px; }
    .muted { color:var(--muted); }
    .stButton button { border-radius:6px; font-weight:700; }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_home():
    st.markdown('<div class="hero"><div class="eyebrow">A calm place to think mathematically</div><h1>Choose the math<br>before doing the math.</h1><p>Sourjya\'s practice studio builds the habit of noticing whether a situation calls for adding, subtracting, multiplying, or dividing.</p></div>', unsafe_allow_html=True)
    st.info('Teacher cue: ask, "What is happening in the story?" before asking, "What is the answer?"')
    st.subheader("Today's path")
    cards = [("01", "Notice the action", "Read a short story and name what is changing."), ("02", "Choose an operation", "Explain why +, -, x, or / matches."), ("03", "Solve and check", "Use a drawing, objects, or a calculator after the idea is clear.")]
    columns = st.columns(3)
    for column, (number, title, copy) in zip(columns, cards):
        with column:
            st.markdown(f'<div class="lesson-card"><div class="number">{number}</div><br><strong>{title}</strong><p class="muted">{copy}</p></div>', unsafe_allow_html=True)
    st.write("")
    left, right = st.columns([1.2, 1])
    with left:
        st.subheader("Start with a quick sort")
        situations = [("There are 3 apples. You get 2 more.", "Add (+)", "the amount grows"), ("You have 8 stickers and give away 3.", "Subtract (-)", "the amount gets smaller"), ("4 bags have 2 blocks in each bag.", "Multiply (x)", "equal groups repeat"), ("10 crackers are shared equally by 2 people.", "Divide (/)", "a group is shared equally")]
        score = 0
        for index, (story, answer, reason) in enumerate(situations):
            choice = st.selectbox(story, ["Choose...", "Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], key=f"home_sort_{index}")
            if choice != "Choose...":
                if choice == answer:
                    score += 1
                    st.success(f"Yes. This is the right operation because {reason}.")
                else:
                    st.warning("Pause and picture the story again. What is happening to the groups or amount?")
        st.caption(f"Sort score: {score}/4. The explanation matters more than the score.")
    with right:
        st.markdown('<div class="tip-card"><div class="eyebrow">Teacher lens</div><h3>Listen for the language</h3><p><b>Add:</b> altogether, more, join</p><p><b>Subtract:</b> left, fewer, difference</p><p><b>Multiply:</b> equal groups, each, groups of</p><p><b>Divide:</b> shared equally, per group, split</p><p class="muted">These words are clues, not rules. Let the story decide.</p></div>', unsafe_allow_html=True)


def render_dates():
    st.markdown('<div class="hero"><div class="eyebrow">Everyday math</div><h1>Calendar dates</h1><p>Read the parts of a date, say the month name, and connect dates to real events.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="date-example">11.22.2009 &nbsp; -> &nbsp; November 22, 2009</div>', unsafe_allow_html=True)
    st.write("")
    month_names = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    st.subheader("Try it")
    date_items = [("11.22.2009", "November 22, 2009"), ("09.16.2026", "September 16, 2026"), ("07.04.2025", "July 4, 2025"), ("02.14.2027", "February 14, 2027")]
    for index, (numeric, correct) in enumerate(date_items):
        month, day, year = numeric.split(".")
        answer = st.text_input(f"Read {numeric} in words", key=f"date_{index}", placeholder="Month day, year")
        if answer:
            if answer.strip().lower() == correct.lower():
                st.success("Correct. You matched month, day, and year.")
            else:
                st.info(f"Check the parts: {month_names[int(month)]} + {int(day)} + {year}.")
    st.subheader("Build a date")
    c1, c2, c3 = st.columns(3)
    with c1:
        month = st.selectbox("Month", list(month_names.values()), index=8)
    with c2:
        day = st.number_input("Day", min_value=1, max_value=31, value=16)
    with c3:
        year = st.number_input("Year", min_value=2000, max_value=2100, value=2026)
    month_number = list(month_names.values()).index(month) + 1
    st.markdown(f'<div class="answer">Numeric date: <b>{month_number:02d}.{day:02d}.{year}</b></div>', unsafe_allow_html=True)


def render_operations():
    st.markdown('<div class="hero"><div class="eyebrow">Concept practice</div><h1>What operation fits?</h1><p>Say what is happening first. Then choose the operation. The answer can come last.</p></div>', unsafe_allow_html=True)
    prompts = [("There are 5 birds on a fence. 2 more land. How many birds are there now?", "Add (+)", "The group gets bigger."), ("Sourjya has 9 crayons and gives 4 away. How many are left?", "Subtract (-)", "The group gets smaller."), ("There are 3 plates with 4 cookies on each plate. How many cookies altogether?", "Multiply (x)", "Equal groups repeat."), ("12 blocks are shared equally into 3 groups. How many blocks in each group?", "Divide (/)", "A total is shared equally."), ("There are 0 groups with 2 items in each group. How many items?", "Multiply (x)", "Zero groups means zero items: 0 x 2 = 0."), ("There are 0 apples, then 2 apples are added. How many apples?", "Add (+)", "Adding 2 to zero gives 2: 0 + 2 = 2.")]
    for index, (story, correct, reason) in enumerate(prompts):
        st.markdown(f'<div class="prompt"><small>Situation {index + 1}</small><br><b>{story}</b></div>', unsafe_allow_html=True)
        choice = st.radio("Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], horizontal=True, key=f"operation_{index}")
        if st.button("Check thinking", key=f"check_{index}"):
            if choice == correct:
                st.success(f"Yes: {reason}")
            else:
                st.error("Not this time. Draw the groups or act out the story, then notice whether items join, leave, repeat, or share.")


def render_operation_practice(operation):
    operation_details = {
        "Addition": {
            "symbol": "+",
            "description": "Addition joins amounts or tells how many there are altogether.",
            "why": ["The amount gets bigger or two groups join.", "The amount is shared equally.", "Equal groups repeat."],
            "problems": [("Sourjya has 3 blue blocks and gets 4 red blocks. How many blocks altogether?", 7), ("There are 5 birds in a tree. 2 more arrive. How many birds now?", 7), ("A box has 0 pencils. 2 pencils are put in. How many pencils?", 2)],
        },
        "Subtraction": {
            "symbol": "-",
            "description": "Subtraction takes away, finds what remains, or compares two amounts.",
            "why": ["The amount gets smaller or we find the difference.", "Two equal groups repeat.", "A total is shared equally."],
            "problems": [("There are 9 crayons. Sourjya gives 3 away. How many remain?", 6), ("There are 8 cookies and 5 are eaten. How many are left?", 3), ("There are 6 red counters and 2 blue counters. How many more red counters?", 4)],
        },
        "Multiplication": {
            "symbol": "x",
            "description": "Multiplication describes equal groups or the same amount repeated.",
            "why": ["Equal groups repeat the same amount.", "One group gets bigger by joining another.", "A total is shared equally."],
            "problems": [("There are 3 bags with 2 blocks in each bag. How many blocks?", 6), ("There are 4 plates with 3 cookies on each plate. How many cookies?", 12), ("There are 0 groups with 5 items in each group. How many items?", 0)],
        },
        "Division": {
            "symbol": "/",
            "description": "Division shares one total into equal groups or finds how many are in each group.",
            "why": ["A total is shared equally.", "The amount gets bigger.", "Equal groups repeat."],
            "problems": [("12 blocks are shared equally into 3 groups. How many in each group?", 4), ("10 crackers are shared equally by 2 people. How many per person?", 5), ("8 counters are put into groups of 4. How many groups?", 2)],
        },
    }
    details = operation_details[operation]
    st.markdown(f'<div class="hero"><div class="eyebrow">{operation} practice</div><h1>Understand {operation.lower()} first.</h1><p>{details["description"]} Choose the reason before entering the answer.</p></div>', unsafe_allow_html=True)
    for index, (story, correct_answer) in enumerate(details["problems"]):
        st.markdown(f'<div class="prompt"><small>Problem {index + 1}</small><br><b>{story}</b></div>', unsafe_allow_html=True)
        reason = st.radio("Why does this operation fit?", details["why"], key=f"{operation}_reason_{index}")
        answer = st.number_input("Answer", min_value=0, step=1, key=f"{operation}_answer_{index}")
        if st.button("Check", key=f"{operation}_check_{index}"):
            if reason == details["why"][0] and answer == correct_answer:
                st.success(f"Correct. {correct_answer} {details['symbol']} is the matching operation and answer.")
            elif answer == correct_answer:
                st.warning("The number is correct. Now explain why this operation fits the story.")
            else:
                st.info("Act out the story with counters or a drawing. Decide what is happening before recalculating.")


def render_week_activity(week_index):
    page_titles = ["Week 1 · Sep 16", "Week 2 · Sep 23", "Week 3 · Sep 30", "Week 4 · Oct 7", "Week 5 · Oct 14", "Week 6 · Oct 21", "Week 7 · Oct 28", "Week 8 · Nov 4", "Week 9 · Nov 11", "Week 10 · Nov 18", "Week 11 · Nov 25", "Week 12 · Dec 2"]
    focus_names = ["Calendar dates", "Addition", "Subtraction", "Operation choice", "Multiplication", "Zero and multiplication", "Addition or multiplication", "Division", "Operation choice", "All four operations", "Dates and operations", "Mixed review"]
    variant = week_index + 1
    def question(prompt, options, answer, explanation, image_index):
        story_intros = [
            "",
            "At the classroom supply table, Sourjya is organizing materials for an art activity. Some supplies are blue, some are red, and the teacher has already placed a few items in a tray. Think about what changes in the story.",
            "During clean-up after a busy activity, Sourjya is counting materials while classmates return some items and leave others on the table. Ignore the extra details and focus on what happens to the amount.",
            "A teacher is preparing a class display with books, counters, and cards. Sourjya hears several facts about the display, but only the action in the story tells which operation belongs.",
            "At a building station, the materials are arranged in neat rows and groups. The table also has spare pieces nearby, so pay attention to whether the same-sized group is repeated.",
            "At the building station, some spaces are empty and some groups are full. Sourjya must decide whether zero describes an empty collection or whether items are being added to a collection.",
            "During a classroom game, Sourjya compares two ways of organizing pencils: putting amounts together or making equal groups. The wording may sound similar, so picture the arrangement before choosing.",
            "At snack time, a teacher places a total number of items on the table and wants everyone to receive a fair share. There are extra plates and napkins, but the equal sharing is the key idea.",
            "In a mixed story station, Sourjya reads several everyday situations involving classmates, supplies, and groups. Some details are there to tell a story; identify the action that controls the operation.",
            "During a math challenge, the teacher mixes joining, taking away, equal groups, and fair sharing on the same page. Read all the details before deciding which operation matches.",
            "While planning a class event, Sourjya checks a calendar, counts days, and notices reminders for other activities. Decide whether the event is moving forward, moving backward, or being described by a date.",
            "At the end-of-term math mission, Sourjya reviews stories from the classroom, snack table, calendar, and building station. The numbers are friendly, but the situation must be understood first.",
        ]
        story_tails = [
            "Write or choose the answer that matches the situation, not every number you noticed.",
            "A careful reader explains why the operation fits before calculating.",
            "Use a quick drawing if the words feel crowded.",
        ]
        intro = story_intros[week_index]
        tail = story_tails[image_index % len(story_tails)]
        if intro:
            expanded_prompt = f"{intro} {prompt} {tail}"
        else:
            expanded_prompt = prompt  # No wrapper, no tail for calendar exercise
        return {"prompt": expanded_prompt, "options": options, "answer": answer, "explanation": explanation}

    if week_index in [0, 10]:
        questions = [
            question("Read 11.22.2009 in words.", ["November 22, 2009", "November 2, 2099", "February 11, 2009", "November 20, 2029"], "November 22, 2009", "The first part is the month, the second is the day, and the last is the year.", 0),
            question("Which month is 09 in 09.16.2026?", ["June", "September", "November", "October"], "September", "09 is the ninth month, September.", 1),
            question("Which part is the day in 07.04.2025?", ["07", "04", "2025", "25"], "04", "The middle part is the day.", 2),
            question("What is 3 days after September 16?", ["September 13", "September 16", "September 19", "October 16"], "September 19", "Moving forward means adding days.", 3),
            question("What is 2 days before October 10?", ["October 2", "October 8", "October 12", "November 10"], "October 8", "Moving backward means subtracting days.", 0),
            question("Which date is written as November 22, 2009?", ["11.02.2009", "02.11.2009", "11.22.2009", "22.11.2009"], "11.22.2009", "The numeric order is month, day, year.", 1),
            question("A party is 4 days away. 1 day passes. How many days remain?", ["3", "4", "5", "1"], "3", "The number of days remaining gets smaller, so subtract.", 2),
            question("Which operation finds days added to a calendar?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/ )"], "Add (+)", "Adding moves forward on the calendar.", 3),
            question("What year is in 02.14.2027?", ["02", "14", "2027", "27"], "2027", "The year is the last part of the date.", 0),
            question("Which date comes first?", ["September 20", "September 16", "September 25", "October 1"], "September 16", "Earlier dates come first when the month is the same.", 1),
        ]
    elif week_index in [1]:
        numbers = [3 + variant, 4 + variant, 5 + variant, 6 + variant, 2 + variant]
        questions = [
            question(f"{numbers[0]} blocks join {numbers[1]} blocks. How many altogether?", [str(numbers[0] + numbers[1] - 1), str(numbers[0] + numbers[1]), str(numbers[0] + numbers[1] + 1), str(numbers[1])], str(numbers[0] + numbers[1]), "The groups join, so add.", 0),
            question(f"Sourjya has {numbers[2]} stickers and gets {numbers[3]} more. How many now?", [str(numbers[2] + numbers[3] - 1), str(numbers[2] + numbers[3]), str(numbers[2] + numbers[3] + 2), str(numbers[3])], str(numbers[2] + numbers[3]), "Getting more makes the amount grow.", 1),
            question(f"What is {numbers[0]} + 0?", [str(numbers[0] - 1), str(numbers[0]), str(numbers[0] + 1), "0"], str(numbers[0]), "Adding zero does not change the amount.", 2),
            question(f"What is 0 + {numbers[4]}?", ["0", str(numbers[4]), str(numbers[4] + 1), str(numbers[4] - 1)], str(numbers[4]), "Adding the group to zero gives that group.", 3),
            question(f"A basket has {numbers[1]} apples. {numbers[4]} more go in. Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Add (+)", "The apples are joining.", 0),
            question(f"What is {numbers[1]} + {numbers[4]}?", [str(numbers[1] + numbers[4] - 1), str(numbers[1] + numbers[4]), str(numbers[1] + numbers[4] + 1), str(numbers[1])], str(numbers[1] + numbers[4]), "Combine both amounts.", 1),
            question(f"There are {numbers[0]} red and {numbers[2]} blue counters. How many counters?", [str(numbers[0] + numbers[2]), str(numbers[2] - numbers[0]), str(numbers[0] * numbers[2]), str(numbers[2])], str(numbers[0] + numbers[2]), "Finding the total means adding.", 2),
            question(f"Which story is addition?", [f"{numbers[0]} more join {numbers[1]}", f"{numbers[0]} leave {numbers[1]}", f"{numbers[0]} groups of {numbers[1]}", f"{numbers[0]} shared equally"], f"{numbers[0]} more join {numbers[1]}", "More items joining is addition.", 3),
            question(f"What number is one more than {numbers[3]}?", [str(numbers[3] - 1), str(numbers[3]), str(numbers[3] + 1), str(numbers[3] + 2)], str(numbers[3] + 1), "One more means add one.", 0),
            question("What should you notice before adding?", ["What is joining or getting more", "How to divide first", "How to make equal groups", "What is leaving"], "What is joining or getting more", "The story tells you when addition fits.", 1),
        ]
    elif week_index in [2]:
        base = 9 + variant
        questions = [
            question(f"There are {base} crayons and 3 are given away. How many remain?", [str(base - 2), str(base - 3), str(base), "3"], str(base - 3), "Giving away makes the amount smaller, so subtract.", 0),
            question(f"{base - 1} birds are on a branch and 2 fly away. How many are left?", [str(base - 3), str(base - 1), str(base + 1), "2"], str(base - 3), "Some birds leave the group.", 1),
            question(f"What is the difference between {base} and 4?", [str(base - 4), str(base + 4), "4", str(base)], str(base - 4), "Difference means compare by subtracting.", 2),
            question(f"What is {base} - 0?", ["0", str(base - 1), str(base), str(base + 1)], str(base), "Taking away zero leaves the amount unchanged.", 3),
            question(f"Which operation fits {base} toys with {variant} put away?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Subtract (-)", "Items are being removed.", 0),
            question(f"What is {base} - {variant}?", [str(base - variant - 1), str(base - variant), str(base + variant), str(variant)], str(base - variant), "Count what remains after some leave.", 1),
            question(f"A shelf has {base - 2} books. {variant} are borrowed. How many remain?", [str(base - 2 - variant), str(base - 2 + variant), str(variant), str(base - 2)], str(base - 2 - variant), "Borrowed books leave the shelf.", 2),
            question("Which story is subtraction?", ["More join", "Some leave", "Equal groups repeat", "A total is shared"], "Some leave", "Subtraction describes an amount getting smaller.", 3),
            question(f"How many more is {base} than {variant}?", [str(base - variant), str(base + variant), str(variant), str(base)], str(base - variant), "More than asks for the difference.", 0),
            question("What should you notice before subtracting?", ["What is leaving or being compared", "What is joining", "How many equal groups", "Who gets a share"], "What is leaving or being compared", "The story tells you when subtraction fits.", 1),
        ]
    elif week_index in [4, 5]:
        groups = 2 + variant % 3
        each = 2 + variant % 2
        questions = [
            question(f"There are {groups} bags with {each} blocks in each. How many blocks?", [str(groups * each - 1), str(groups * each), str(groups + each), str(each)], str(groups * each), "Equal groups repeat, so multiply.", 0),
            question(f"What is {groups} x {each}?", [str(groups + each), str(groups * each), str(groups * each + 1), str(groups)], str(groups * each), "Multiplication counts equal groups.", 1),
            question(f"Which operation matches {groups} groups of {each}?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Multiply (x)", "Groups of means equal groups.", 2),
            question(f"There are {groups + 1} plates with {each + 1} cookies each. How many cookies?", [str((groups + 1) * (each + 1)), str(groups + each + 2), str(groups * each), str(groups + 1)], str((groups + 1) * (each + 1)), "The same number is repeated on every plate.", 3),
            question(f"What is 1 x {each}?", ["0", "1", str(each), str(each + 1)], str(each), "One group has the amount in that group.", 0),
            question("What is 0 x 5?", ["0", "5", "1", "10"], "0", "Zero groups contain zero items.", 1),
            question(f"What is {each} + {each} + {each}?", [str(each * 2), str(each * 3), str(each + 3), str(each)], str(each * 3), "Repeated addition shows three equal groups.", 2),
            question("Which picture idea shows multiplication?", ["Equal groups", "One amount leaving", "A total shared", "Two amounts joining once"], "Equal groups", "Multiplication is about equal groups.", 3),
            question(f"There are {groups} rows of {each} counters. Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Multiply (x)", "Rows with the same number are equal groups.", 0),
            question("What should you notice before multiplying?", ["Equal groups or the same amount repeated", "Something leaving", "A total split fairly", "A date's month"], "Equal groups or the same amount repeated", "The story tells you when multiplication fits.", 1),
        ]
    elif week_index in [7]:
        questions = [
            question("12 blocks are shared equally into 3 groups. How many per group?", ["3", "4", "6", "9"], "4", "Division shares one total equally.", 0),
            question("10 crackers are shared by 2 people. How many each?", ["2", "5", "8", "12"], "5", "Each person gets an equal share.", 1),
            question("Which operation matches fair sharing?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Divide (/)", "Division describes equal sharing.", 2),
            question("8 counters are put into groups of 4. How many groups?", ["2", "4", "8", "12"], "2", "Two groups of four make eight.", 3),
            question("Which story uses division?", ["3 more join", "2 leave", "4 groups of 2", "12 shared equally"], "12 shared equally", "Sharing equally is division.", 0),
            question("What is 6 / 2?", ["2", "3", "4", "8"], "3", "Six shared into two equal groups gives three in each.", 1),
            question("What should you have before dividing?", ["A total to share", "A group that gets bigger", "Equal groups to repeat", "A date"], "A total to share", "Division starts with a total that can be shared.", 2),
            question("What is 9 / 3?", ["2", "3", "6", "12"], "3", "Nine shared into three equal groups gives three.", 3),
            question("Which phrase is a division clue?", ["altogether", "each group gets", "more arrive", "left over after"], "each group gets", "Each group gets points to equal sharing.", 0),
            question("Which operation should we practice after understanding addition and groups?", ["Divide when a total is shared", "Always divide", "Never use groups", "Guess"], "Divide when a total is shared", "Division belongs when the story describes sharing.", 1),
        ]
    else:
        questions = [
            question("5 birds join 2 birds. Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Add (+)", "The group gets bigger.", 0),
            question("9 crayons become 4 after some are given away. Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Subtract (-)", "Some items leave the group.", 1),
            question("3 bags have 2 blocks each. Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Multiply (x)", "Equal groups repeat.", 2),
            question("12 blocks are shared equally into 3 groups. Which operation?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"], "Divide (/)", "A total is shared equally.", 3),
            question("What is 4 + 3?", ["1", "7", "12", "4"], "7", "Two amounts join, so add.", 0),
            question("What is 8 - 3?", ["5", "11", "3", "24"], "5", "Some leave, so subtract.", 1),
            question("What is 3 x 2?", ["5", "6", "9", "1"], "6", "Three groups of two make six.", 2),
            question("What is 10 / 2?", ["2", "5", "8", "12"], "5", "Ten shared by two gives five each.", 3),
            question("What should happen before calculation?", ["Choose the operation from the story", "Always multiply", "Always divide", "Skip the story"], "Choose the operation from the story", "Understanding the situation comes first.", 0),
            question("Which operation fits equal groups?", ["Add (+)", "Subtract (-)", "Multiply (x)", "Only division"], "Multiply (x)", "Equal groups repeat the same amount.", 1),
        ]

    page_title = page_titles[week_index]
    title = WEEK_TAB_NAMES[week_index]
    focus = focus_names[week_index]
    current_key = f"week_{week_index}_current"
    score_key = f"week_{week_index}_score"
    submitted_key = f"week_{week_index}_submitted"
    feedback_key = f"week_{week_index}_feedback"
    st.session_state.setdefault(current_key, 0)
    st.session_state.setdefault(score_key, 0)
    st.session_state.setdefault(submitted_key, False)
    st.session_state.setdefault(feedback_key, None)
    current = st.session_state[current_key]
    st.markdown(f'<div class="hero"><div class="eyebrow">{page_title} · {focus}</div><h1>{title}</h1><p>One question at a time. Choose an answer, submit it, and explain your thinking.</p></div>', unsafe_allow_html=True)
    score_col, progress_col = st.columns([1, 3])
    with score_col:
        st.metric("Score", f"{st.session_state[score_key]} / {len(questions)}")
    with progress_col:
        st.progress((current + (1 if st.session_state[submitted_key] else 0)) / len(questions), text=f"Question {current + 1} of {len(questions)}")
    item = questions[current]
    st.markdown(f'<div class="prompt"><small>Question {current + 1}</small><br><b>{item["prompt"]}</b></div>', unsafe_allow_html=True)
    st.radio("Choose one answer", item["options"], key=f"week_{week_index}_choice_{current}", disabled=st.session_state[submitted_key])
    if st.button("Submit answer", key=f"week_{week_index}_submit_{current}", disabled=st.session_state[submitted_key], type="primary"):
        selected = st.session_state[f"week_{week_index}_choice_{current}"]
        correct = selected == item["answer"]
        if correct:
            st.session_state[score_key] += 1
        st.session_state[feedback_key] = (correct, selected, item["answer"], item["explanation"])
        st.session_state[submitted_key] = True
        st.rerun()
    feedback = st.session_state[feedback_key]
    if feedback:
        correct, selected, answer, explanation = feedback
        if correct:
            st.success("🎉 Correct! Great thinking. You chose the answer that matches the story.")
        else:
            st.error(f"Not quite. The correct answer is **{answer}**.")
            st.info(f"Why: {explanation}")
        if current < len(questions) - 1:
            if st.button("Next problem", key=f"week_{week_index}_next_{current}", type="primary"):
                st.session_state[current_key] += 1
                st.session_state[submitted_key] = False
                st.session_state[feedback_key] = None
                st.rerun()
        else:
            st.balloons()
            st.success(f"Deck complete! Final score: {st.session_state[score_key]} / {len(questions)}.")
            if st.button("Restart this date's deck", key=f"week_{week_index}_reset"):
                st.session_state[current_key] = 0
                st.session_state[score_key] = 0
                st.session_state[submitted_key] = False
                st.session_state[feedback_key] = None
                for question_index in range(len(questions)):
                    st.session_state.pop(f"week_{week_index}_choice_{question_index}", None)
                st.rerun()


def render_schedule():
    st.markdown('<div class="hero"><div class="eyebrow">Table of contents · Wednesday studio plan</div><h1>Choose a Wednesday.</h1><p>Classes resume Wednesday, September 16, 2026 at 7:00 PM. Each session below links directly to the activity for that day.</p></div>', unsafe_allow_html=True)
    start = date(2026, 9, 16)
    weeks = [("Decode the Date", "Read numeric dates; say month, day, year; make a personal calendar connection."), ("More to Explore", "Act out addition stories with objects; choose + before solving."), ("What's Left?", "Act out subtraction stories; compare what changed and what remains."), ("Operation Sleuths", "Sort mixed stories and explain the change in words."), ("Group Groove", "Build groups with counters; connect repeated groups to multiplication."), ("Zero Has a Job", "Compare 0 + 2, 0 - 2, and 0 x 2 with concrete objects."), ("Add It or Group It?", "Contrast 3 + 2 with 3 groups of 2; draw before calculating."), ("Fair Share Crew", "Use objects to share small totals equally; introduce division language."), ("Choose Your Move", "Sort addition, subtraction, and multiplication word problems."), ("Four-Way Math Match", "Add division only when a total is being shared equally."), ("Calendar Countdown", "Read dates, count days to an event, and choose an operation."), ("Math Mission Finale", "Mixed word-problem game; explain the operation before using a calculator.")]
    for index, (title, activity) in enumerate(weeks):
        session_date = start + timedelta(days=index * 7)
        details, link = st.columns([4, 1])
        with details:
            st.markdown(f"**{session_date.strftime('%A, %B %d, %Y')} at 7:00 PM**  \n**{title}** - {activity}")
        with link:
            if st.button("Open activity", key=f"schedule_activity_{index}"):
                st.session_state.next_page = WEEK_TAB_NAMES[index]
                st.rerun()
        if index < len(weeks) - 1:
            st.divider()
    st.caption("This is a rough sequence. It can slow down, repeat, or skip ahead based on what Sourjya explains aloud.")


st.sidebar.markdown("# Math Quest Studio")
st.sidebar.caption("Meaning first. Numbers second.")
if "next_page" in st.session_state:
    st.session_state.page = st.session_state.pop("next_page")
page_options = ["Home", "Wednesday plan"]
page_options += WEEK_TAB_NAMES
page = st.sidebar.radio("Go to", page_options, key="page")
st.sidebar.divider()
st.sidebar.markdown("**Class rhythm**")
st.sidebar.write("1. Read or act out the story")
st.sidebar.write("2. Name what is happening")
st.sidebar.write("3. Choose the operation")
st.sidebar.write("4. Solve and explain")

if page == "Home":
    render_home()
elif page in WEEK_TAB_NAMES:
    render_week_activity(WEEK_TAB_NAMES.index(page))
elif page == "Calendar dates":
    render_dates()
elif page in ["Addition", "Subtraction", "Multiplication", "Division"]:
    render_operation_practice(page)
elif page == "Operation choice":
    render_operations()
else:
    render_schedule()