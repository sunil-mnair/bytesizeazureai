import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from pprint import pprint

from services import detect_language_service,analyze_facial_attributes,extract_entity_information,extract_handwritten_text,extract_image_descriptions,detect_sentiment_extract_key_phrases

app = Flask(__name__)

getcwd = os.getcwd()

@app.route('/')
def index():
   
   return render_template('index.html')



# Language Service - Language Detection
@app.route("/detect_language",methods=['GET','POST'])
def detect_language():

    text = ''
    result = ''
    language = ''

    score = 0

    if request.method == "POST":
        text = request.form["sampleText"]
        result = detect_language_service.detect_language_fn(text)

    if result:
        language = result['documents'][0]['detectedLanguage']['name']
        score = result['documents'][0]['detectedLanguage']['confidenceScore']

    return render_template("detect_language.html",
                           language=language,score=score)

# Language Service - Entity Information
@app.route("/entity_information",methods=['GET','POST'])
def entity_information():

    text = ''
    result = ''
    lang =''

    if request.method == "POST":
        text = request.form["sampleText"]
        lang = 'en'

        result = extract_entity_information.entity_information(lang,text)

    print(result)

    return render_template("detect_language.html",result=result)


# Language Service - Sentiment Analysis and Key Phrases
@app.route("/sentiment_analysis_key_phrases",methods=['GET','POST'])
def sentiment_analysis_key_phrases():

    text = ''
    result = ''
    lang =''
    sentiment = ''
    key_phrases =''

    if request.method == "POST":
        text = request.form["sampleText"]
        lang = 'en'

        result = detect_sentiment_extract_key_phrases.sentiment_analysis_key_phrases(lang,text)

    if result:
        sentiment,key_phrases = result 

        print(sentiment)
        print(key_phrases)

    return render_template("sentiment_analysis.html",sentiment=sentiment,key_phrases=key_phrases)





# Bot Service
@app.route('/chatbot')
def chatbot():
    bot_name = "The Bot"
    return render_template('chatbot.html',display = bot_name)


# OCR - Handwritten Text Recognition
@app.route("/handwriting_recognition",methods=['GET','POST'])
def handwriting_recognition():
    result = ''
    status = 0
    image = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive-services/Computer-vision/Images/readsample.jpg "

    try:
        result,status = extract_handwritten_text.handwritten_text(image)
    except:
        print("End Point and Key have not been provided")

    if status:
        # Print the detected text, line by line
        for text_result in result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                print(line.bounding_box)
    

    return render_template("handwriting_recognition.html",
                           result=result)

@app.route("/image_description",methods=['GET','POST'])
def image_description():

    result =''

    image = "https://revivre-notre-dame.fr/wp-content/uploads/2021/11/DR-notre-dame-5310767_1920-1024x683.jpg"

    try:
        result = extract_image_descriptions.caption_images(image)
    except:
        print("End Point and Key not provided")

    if result:
        # Get the captions (descriptions) from the response, with confidence level
        print("Description of remote image: ")
        if len(result.captions) == 0:
            print("No description detected.")
        else:
            for caption in result.captions:
                print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
        print()
    

    return render_template("image_desc.html",
                           result=result)


# Face API
@app.route("/facial_attributes",methods=['GET','POST'])
def facial_attributes():

    text = ''
    result = ''
    language = ''

    score = 0

    image_path = os.path.join(getcwd+'/static/images/CapFrame.jpg')
    print(image_path)
    image_data = open(image_path, "rb")


    if request.method == "POST":
        text = request.form["sampleText"]
        result = analyze_facial_attributes.facial_attributes(image_data)

    if result:
        print(result)

    return render_template("facial_attributes.html",
                           result=result)




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)

