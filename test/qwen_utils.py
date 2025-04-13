import json
from transformers import Qwen2_5_VLProcessor
from vision_process import process_vision_info

# default processer
# from given config file
# processor = Qwen2_5_VLProcessor.from_config(r"config\qwen25vl_7b.json")

# The default range for the number of visual tokens per image in the model is 4-16384.
# You can set min_pixels and max_pixels according to your needs, such as a token range of 256-1280, to balance performance and cost.
min_pixels = 256 * 28 * 28
max_pixels = 1280 * 28 * 28
processor = Qwen2_5_VLProcessor.from_pretrained(
    "Qwen/Qwen2.5-VL-3B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": r"file://C:\Users\yigua\Downloads\Bon Iver - Everything Is Peaceful Love (Official Video)-1.mp4",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs, video_kwargs = process_vision_info(
    messages, return_video_kwargs=True
)
print(video_kwargs)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
    **video_kwargs,
)
print(inputs["second_per_grid_ts"])
# inputs = inputs.to("cuda")

# # Inference: Generation of the output
# generated_ids = model.generate(**inputs, max_new_tokens=128)
# generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
# output_text = processor.batch_decode(
#     generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
# )
# print(output_text)
