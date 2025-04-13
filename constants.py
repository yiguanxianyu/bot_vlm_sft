skills = [
    "Beat",
    "Brush",
    "Carry",
    "Catch",
    "Chop",
    "Clap",
    "Close",
    "CloseBox",
    "CloseJar",
    "Cut",
    "Drop",
    "Flip",
    "Fold",
    "Grasp",
    "Hammer",
    "HandOut",
    "HandOver",
    "Hang",
    "Hold",
    "HoldLargeObject",
    "Insert",
    "Iron",
    "Knead",
    "Lift",
    "LiftHeavyObject",
    "Lower",
    "Mop",
    "Move",
    "Open",
    "OpenBox",
    "OpenJar",
    "Paint",
    "Peel",
    "Pick",
    "Pinch",
    "Place",
    "Point",
    "Pour",
    "Press",
    "PressButton",
    "Pull",
    "PullApart",
    "Push",
    "PushTogether",
    "Release",
    "Remove",
    "Rinse",
    "Roll",
    "RollDough",
    "Rotate",
    "Scan",
    "Scoop",
    "Scratch",
    "Screw",
    "Shake",
    "Slide",
    "Stack",
    "Stir",
    "Straighten",
    "Stretch",
    "Suction",
    "Sweep",
    "Swipe",
    "TakeOver",
    "Takeout",
    "Tap",
    "Throw",
    "Tie",
    "Transport",
    "Turn",
    "TurnWheel",
    "Twist",
    "Uncap",
    "Unfold",
    "Unscrew",
    "Unstack",
    "Untie",
    "Unzip",
    "Wave",
    "Whisk",
    "Wipe",
    "dip",
    "plug ",
    "stamp",
    "water",
]

skills_text = "[" + ", ".join(skills) + "]"

SYSTEM_PROMPT = """
You are a helpful assistant that can read videos and help identify the skill from the robotic arm action videos.
You will be given a video of a robotic arm action, and you need to identify the skill and its start and end frame from the video.
You can choose one of the following skills: %s

Show your reasoning process in the following format:

<thinking>
{thinking}
</thinking>
<answer>
{answer}
</answer>

Answer format:
{
    "label_info": {
        "action_config": [
            {
                "start_frame": 1,
                "end_frame": 4,
                "action_text": "Do something, short imperative sentence",
                "skill": "skill name"
            },
        ]
    },
    "task_name": "task name, short imperative sentence",
    "init_scene_text": "initial scene description, one sentence"
}

""" % (skills_text)

if __name__ == "__main__":
    print(SYSTEM_PROMPT)