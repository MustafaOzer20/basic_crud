
class Memory():
    all_data = []
    def create(self, json):
        (_, index) = self.find_data(id=json["id"])
        if index != -1:
            return {
                "Error":"ID unique olmali"
            }
        self.all_data.append(json)

    def update(self, id, new_json):
        (_, index) = self.find_data(id)
        if index == -1:
            return {
                "Error":"Veri Yok"
            }

        self.all_data[index] = new_json

    def delete(self, id):
        (_, index) = self.find_data(id)
        if index == -1:
            return {
                "Error":"Veri Yok"
            }

        self.all_data.pop(index)
        return {
            "success": "Veri Silindi"
        }
        
        
    def find_data(self, id):
        counter = 0
        for json in self.all_data:
            if id == json['id']:
                return (json,counter)
            counter += 1
        return (-1,-1)

    def get_data(self):
        return self.all_data
        

memory = Memory()

class ExampleData():
    # id, title, problem, point, level, language, input, expected_output
    
    data = {}
    def __init__(self, id, title, problem, point, level, language, input, expected_output):
        self.data = {
            "id": id,
            "title": title,
            "problem": problem,
            "point": point,
            "level": level,
            "language": language,
            "input": input,
            "expected_output": expected_output
        }
    def save(self):
        global memory
        memory.create(self.data)




ex = ExampleData(
    id="3136e3cd-c90c-48bb-b9a9-60ca68382ad7", 
    title="Say hello with python",
    problem="Print hello world in Python using print",
    point=1, level="beginner", language="python", input="", expected_output="Hello World"
    )

ex.save()

ex2 = ExampleData(
    id="1ff26d62-e748-4907-bccf-cf2eec4ec06b",
    title="Arithmetic Operators - Sum",
    problem="Sum two numbers",
    point=2, level="beginner", language="python", input="5,6", expected_output="11"
    )

ex2.save()

ex3 = ExampleData(
    id="d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
    title="Loops",
    problem="Print the square of each number in the loop step",
    point=2, level="beginner", language="python", input="4", expected_output="0,1,4,9"
    )

ex3.save()


print(memory.get_data())






