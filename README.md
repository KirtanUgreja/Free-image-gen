# 🌥️ AI Image Generator using A4F API

Generate **stunning AI images** just by writing a prompt!  
This project uses the [A4F API](https://a4f.co) to create AI-generated visuals and automatically download them into your local `images/` folder.

🔗 **Repo**: [KirtanUgreja/Image-gen-using-api](https://github.com/KirtanUgreja/Image-gen-using-api)

---

## 🚀 Features

- 🧠 Powered by `provider-4/imagen-3` model
- ✍️ Convert text prompts to high-quality 1024x1024 images
- 📥 Downloads and saves each image with a unique name
- 📁 All images stored neatly in the `images/` directory

---

## 🛠️ Setup & Installation

### 1. Clone this repository

```bash
git clone https://github.com/KirtanUgreja/Image-gen-using-api.git
cd Image-gen-using-api
```

### 2. Install required packages

```bash
pip install requests
```

### 3. Add your API key
Replace the following line in the code:
```bash
"Authorization": 'Bearer A4F-api-key'(insted of A4F-api-key insert your do not remove 'Bearer')
```

## 💡 How to Run
Make sure you have a folder named images in the same directory. If not:

```bash
mkdir images
```
Then run the script:
```bash
python imagen-gen.py
```
The generated image will be downloaded to the images/ folder with a unique name like:
```bash
images/generated_image_abcd1234.png
```


## ✨ Example Prompts & Results

### 🧑‍💻 Prompt 1: laptop in the clouds
<img src="https://github.com/KirtanUgreja/Image-gen-using-api/blob/main/images/generated_image_d6688846.png?raw=true" width="40%" alt="Laptop in the clouds" />

### 🚗 Prompt 2: car in the clouds
<img src="https://github.com/KirtanUgreja/Image-gen-using-api/blob/main/images/generated_image_bcc0d62c.png?raw=true" width="40%" alt="Car in the clouds" />


## 🤝 Want to Contribute?
### Contributions are welcome!
- 🍴 Fork this repository
- 📦 Create a feature branch
- 🔧 Make your improvements
- 📤 Submit a pull request

Let’s build cool tools together! 💡✨

## 📩 Contact
### Have questions, suggestions, or feedback? Feel free to open an issue.
