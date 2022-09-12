import re

def main():
    #res = re.split(" |,","Prova ciao,ciao")
    #print(res)
    traduce_dataset("train.txt","tr/")
    traduce_dataset("test.txt","tr/")
    traduce_dataset("valid.txt","tr/")
    create_entities_and_rel("train.txt","tr/")
    

def traduce_dataset(path, save_path):
    f = open(path, "r")
    fw = open(save_path+path,"w")
    for line in f:
        res = re.split("\(|\)|,",str(line))
        fw.write(res[1]+"\t"+res[0]+"\t"+res[2]+"\n")

def create_entities_and_rel(path, save_path):
    f = open(path,"r")
    fw = open(save_path+"entities.dict","w")
    fw1 = open(save_path+"relations.dict","w")
    entities = []
    rels = []
    for line in f:
        res = re.split("\(|\)|,",str(line))
        entities.append(res[1])
        entities.append(res[2])
        rels.append(res[0])
    entities = set(entities)
    rels = set(rels)
    i = 0
    j = 0
    for ent in entities:
        fw.write(str(i)+"\t"+ent+"\n")
        i+=1
    for rel in rels:
        fw1.write(str(j)+"\t"+rel+"\n")
        j+=1 
if __name__=="__main__":
    main()
