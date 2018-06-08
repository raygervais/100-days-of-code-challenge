//
//  ViewController.swift
//  Breed-List
//
//  Created by Ray Gervais on 2018-06-07.
//  Copyright © 2018 Ray Gervais. All rights reserved.
//

import UIKit

class ViewController: UITableViewController {
    let location: String = "https://dog.ceo/api/"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        getDogBreedList()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // Web Request
    func getDogBreedList() {
        let api: String = "breeds/list/all"
        
        guard let url = URL(string: location + api) else {
            print("Error: cannot create URL from api specified")
            return
        }
        
        let request = URLRequest(url: url)
        
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
        
        // Make Request
        let task = session.dataTask(with: request) {
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
                
                print("Status \(status)")
                
                let res = apiData["message"] as! NSDictionary
                for item in res {
                    print(item.key)
                }
                
            } catch let parseError as NSError {
                print(parseError.userInfo)
            }
        }
        task.resume()

    }
}

