//
//  ViewController.swift
//  Breed-List
//
//  Created by Ray Gervais on 2018-06-07.
//  Copyright © 2018 Ray Gervais. All rights reserved.
//

import UIKit

class ListViewController: UITableViewController, WebServiceModelDelegate {
    
    var model: WebServiceModel!

    
    func webServiceModelDidChangeContent(model: WebServiceModel) {
        tableView.reloadData()
    }

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Dog Breeds"
        self.tableView.rowHeight = 70.0

        model.delegate = self
        
        model.get(type: "Breed")

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    // You can use this code as-is, it should handle most cases
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return model.breedResults.count
    }
    
    // You can use this code as-is, it should handle most cases
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath) as UITableViewCell
        self.configure(cell: cell, atIndexPath: indexPath)
        return cell
    }
    
    // Code you will customize to setup the cell
    func configure(cell: UITableViewCell, atIndexPath indexPath: IndexPath) {
        cell.textLabel!.text = model.breedResults[indexPath.row].capitalized
        
    }

}

