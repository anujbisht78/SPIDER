import requests

# hugging face API
api="Your API Key"

# create an img gen Func
def img_genertor(prompt,output_file):
    
    API_URl = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    
    headers={"Authorization": f"Bearer {api}"}
    
    def query(payload):
        response=requests.post(API_URl, headers=headers, json=payload)
        return response.content
    
    image_bytes=query({
        "inputs" : prompt,
    })
    
    with open(output_file,"wb") as f:
        f.write(image_bytes)


# if __name__ == "__main__":
#     img_gen("Generate an image of a room which consits many closets and its interior should be very unique","gen_img.png")


