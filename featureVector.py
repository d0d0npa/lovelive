#!coding:utf-8
'''
Created on 2017/06/07

@author: KentoK
'''
import csv
import os
import sys
import random

class IdolList:
    '''
    @note: アイドルたちのリスト
    @param idols:Idolクラスが入っているリスト
    @param attributes:特徴ベクトルのそれぞれの次元の名前のリスト
    '''
    def __init__(self,attribute):
        self.idols = []#アイドルたち
        self.attributes = attribute#特徴の名前

    def appendIdol(self,idol):
        '''
        @note: アイドルを追加
        @param idol:Idolクラスのインスタンス
        @type idol:Idolクラス
        '''
        self.idols.append(idol)

    def showIdols(self):
        for i in self.idols:
            i.showIdol()

    def outputCSV(self,outputFile):#
        '''
        @note: 全てのアイドルの特徴量をCSVファイルとして出力
        @param outputFile:CSVファイルの出力する場所を指定
        '''
        print("CSV出力開始　出力場所：" + outputFile)
        f = open(outputFile + '.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')
        attribute  = ["IdolName","IdolFileName"]
        attribute.extend(self.attributes)
        writer.writerow(attribute)

        for i in self.idols:
            eachRow = []
            eachRow.append(i.getIdolName())
            eachRow.append(i.getIdolFileName())
            for j in range(i.numFeatures):
                eachRow.append(i.getFeatureVec(j))
            #print (eachRow)
            writer.writerow(eachRow)
        f.close()
        print("CSV出力完了")

class Idol:
    numFeatures = 0 #特徴ベクトルの次元数
    featureAttribute = []#特徴ベクトルのそれぞれの次元の名前
    totalIdols = 0 #生成したアイドルの合計数

    def __init__(self,numFeatures):
        self.features = []
        self.idolName = ""#アイドルの名前
        self.idolFileName = ""#アイドルの画像ファイル名
        Idol.numFeatures = numFeatures
        for i in range(Idol.numFeatures):
            self.features.append(0)
        Idol.totalIdols += 1

    def setIdolName(self,name):
        '''
        @note: アイドルの名前をセットする
        @param name : アイドルの名前
        @type name: String
        '''
        self.idolName = name

    def getIdolName(self):
        return self.idolName

    def setIdolFileName(self,name):
        '''
        @note: アイドルの画像ファイル名をセットする
        @param name : アイドルの画像ファイル名
        @type name: String
        '''
        self.idolFileName = name

    def getIdolFileName(self):
        return self.idolFileName

    def setFeatureVec(self,featureVec,element):#
        '''
        @note: i次元目の特徴ベクトル(featureVec)にある値（element）をセットする
        @param featureVec : i次元
        @type featureVec: int
        @param element: セットする値
        '''
        self.features[featureVec] = element

    def getFeatureVec(self,featureVec):
        return self.features[featureVec]

    def randomizeFeatureVec(self):
        '''
        @note: 特徴ベクトルの全ての次元を0か1の値にランダムに設定する
        '''
        for i in range(Idol.numFeatures):
            self.features[i] = random.randint(0,1)

    def showIdol(self):
        print("IdolName:" + self.idolName)
        print("IdolFileName:" + self.idolFileName)
        print("IdolAttributes:")
        for i in range(Idol.numFeatures):
            print("/t Attribute " + str(i) + " : " + str(self.features[i]))

if __name__ == '__main__':
    outputDir = os.path.dirname(os.path.abspath(__file__))#出力ディレクトリ（カレントディレクトリ）
    outputFile = "feature" #出力するファイル名
    output = os.path.join(outputDir , outputFile) #出力場所の絶対パス
    numFeatures = 2#特徴ベクトルの次元数
    featureVectorName = ["Feature_A","Feature_B"]#それぞれの次元の名前
    '''
    @note: 特徴量の候補：髪の長さ、身長、目の色が暖色か寒色か、年齢（１０代か２０代か）
    '''

    if os.name == 'posix':
        #(Linuxの場合の処理）
        files = os.listdir('./photo')#写真フォルダ内のファイルのリスト
    elif os.name == 'nt':
        #(Windowsの場合の処理）
        files = os.listdir('.¥¥photo')#写真フォルダ内のファイルのリスト

    photoList = files#写真のリスト
    #print("ディレクトリ内のファイル")
    #print(photoList)

    idolList = IdolList(featureVectorName)#アイドルのリストを作成

    #取得したキャラごとにとりあえず何かを作る
    for i, x in enumerate(photoList):
        oneIdol = Idol(numFeatures = numFeatures)#一人のアイドルのインスタンスを生成
        oneIdol.featureAttribute = featureVectorName#featureAttributeなのでいらない
        oneIdol.setIdolFileName(x)#アイドルの画像ファイル名
        oneIdol.randomizeFeatureVec()#特徴ベクトルの全要素を0か1のいずれかの値に設定
        '''
        for j in range(numFeatures):
            oneIdol.setFeatureVec(featureVec = j, element = 0)
        '''
        idolList.appendIdol(oneIdol)

    #idolList.showIdols()
    #適当にCSV出力
    idolList.outputCSV(outputFile = output)

    sys.exit()
