//
//  Breeds.swift
//  Breed-List
//
//  Created by Ray Gervais on 2018-06-09.
//  Copyright © 2018 Ray Gervais. All rights reserved.
//

import Foundation

class Breed {
    var name: String
    var subBreeds: [String]?
    
    init(data :Dictionary<String, String>) {
        print(data)
        
        name = ""
    }
   
}
