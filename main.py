from data_load import DataLoad

class Main:

    def load_data(self):
        data_load: DataLoad = DataLoad()
        data_load.load()

    
    def run(self):
        print("Staring Main...")
        pass




if __name__ == "__main__":
    Main().run()
