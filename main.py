# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:37:08 2019

@author: Harrish Selvarajah
"""
from movieCF import movieCF
from novelCF import novelCF
from morvelrecc import morvelrecc
from ContentRecs import ContentRecs
from NovelFinder import NovelFinder
#import Neuralmovie.HybridTest 
# =============================================================================
# import Neuralnovel.HybridTest
# import surprise
# =============================================================================

from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_start():#colloborative filtering 
    return "Flask API" #pass the userID

@app.route('/getcfmovies/<userid>', methods=['GET'])
def get_cfmovies(userid):#colloborative filtering 
    obj1 = movieCF()
    #id = '70'
    return jsonify({'cfmoviearray': obj1.computeMovieCf(userid)}) #pass the userID

@app.route('/getcfnovels/<userid>', methods=['GET'])
def get_cfnovels(userid):#colloborative filtering code for novels
    return jsonify({'cfnovelarray':novelCF.computeNovelCf(userid)})  #pass the userID

@app.route('/getnovelreco', methods=['GET']) #2 mins
def get_movietonovel():#moveitonovel reco
    obj = morvelrecc()
    return jsonify({'cfmovietonovelarray': obj.computesimilarityscore()}) 

@app.route('/getcontentfmovies/<userid>', methods=['GET'])
def get_contentfmovies(userid):#content filtering 
    obj2 = ContentRecs()
    return jsonify({'cfmoviearray': obj2.contentf(userid)}) #pass the userID

@app.route('/getnovelformovie/<moviename>', methods=['GET'])
def get_novelformovie(moviename):#he novel for the corresponding movie
    obj3 = NovelFinder()
    return jsonify({'cfmoviearray': obj3.computesimilarnovel(moviename)}) #pass the Movie Name

#NEURAL-----    

# =============================================================================
# @app.route('/getnovel/<userid>', methods=['GET'])
# def getNovel(userid):#colloborative filtering 
#     (predictions, algo) = surprise.dump.load('./NeuralNovelReco/HybridDump.pkl')
#     return jsonify(NeuralNovelReco.HybridTest.predictions(userid,algo)) #pass the userID
# 
# @app.route('/settrain', methods=['GET'])
# def trainNovel():#colloborative filtering 
#     NeuralNovelReco.HybridTest.trainModel()
#     return "Done"
# =============================================================================




if __name__ == '__main__':
    app.run(debug=True)




