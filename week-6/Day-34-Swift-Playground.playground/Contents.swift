//: Playground - noun: a place where people can play

import UIKit
import PlaygroundSupport


var str = "Hello, playground"


func makeHTTPGetRequest() {
    let endPoint: String = "https://dog.ceo/api/breed/beagle/images"
    guard let url = URL(string: endPoint) else {
        print("Error: cannot create URL from specified")
        return
    }
    
    let urlRequest = URLRequest(url: url)
    
    // Session Configuration
    let config = URLSessionConfiguration.default
    let session = URLSession(configuration: config)
    
    // Make Request
    let task = session.dataTask(with: urlRequest) {
        (data, response, error) -> Void in
        
        guard error == nil else {
            print("Error: \(error!)")
            return
        }
        
        guard let responseData = data else {
            print("Error: did not recieve any data")
            return
        }
        
        do {
            guard let apiData = try JSONSerialization.jsonObject(with: responseData, options: [])
                as? [String: Any] else {
                    print("Error: cannot convert data to JSON")
                    return
            }
            
            let status: String = apiData["status"] as! String
            let data: [Any] = apiData["message"] as! [Any]
            
            print("Status \(status)")
            print("Returned Breed: \(data.count)")
            
            let smallData = data.first
            let dataURL = NSURL.init(fileURLWithPath: smallData as! String)
            let img = NSData(contentsOf: dataURL as URL)
            
            UIImage(data: img as Data)
           
//            data.map { (dog)  -> UIImage?  in
//                return UIImage(named: dog as! String)
//            }
        }
        
        catch let parseError as NSError {
            print(parseError.domain)
        }
    }
    task.resume()
}

makeHTTPGetRequest()

PlaygroundPage.current.needsIndefiniteExecution = true
