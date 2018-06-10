

protocol WebServiceModelDelegate : class {
    func webServiceModelDidChangeContent(model: WebServiceModel)
}

class WebServiceModel {
    // Property to hold/store the fetched collection
    var breedResults = [String]()
    
    // The delegate gets called to report that the data has changed
    weak var delegate: WebServiceModelDelegate? = nil
    
    init() {    }
    
    func get(type: String) {
        var url = ""
        
        switch type {
        case "Breed":
            url = "breeds/list/all"
        default:
            print("Default")
        }
        
        let request = NetworkController()
        self.breedResults.removeAll()
        
        // Request
        request.sendRequest(toUrlPath: url, dataKeyName: "results", completion: {
            (result: [AnyObject]) in
            
            var tmp = [Dictionary<String, AnyObject>]()
            
                for item in result {
                    guard let res = item as? [String:AnyObject] else {
                        continue
                    }
                    tmp.append(res)
                }
            
            if type == "Breed" {
                var innerTmp = tmp[0] as! Dictionary<String, AnyObject>
                innerTmp = innerTmp["message"] as! Dictionary<String, AnyObject>
                self.breedResults = Array(innerTmp.keys)
                // self.breedResults = self.breedResults.first!["message"] as! Dictionary<String, AnyObject>
            }
            
            
          
            // notify the delegate
            self.delegate?.webServiceModelDidChangeContent(model: self)
        })
    }
}
