const API_URL =  "http://localhost:3000";

//select DOM elements
const userform = document.getElementById('form');
const useridfield = document.getElementById('userid');
const namefield = document.getElementById('name');
const incomefield = document.getElementById('income');
const datalist = document.getElementById ('data');
const tableBody = document.getElementById('dataTable');

let currenttask = null;

//fetch and render details
const fetchdetails = async () => {
    try {
        const response = await fetch(`${API_URL}/details`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);            
        }
        const lists = await response.json();

        //clear the current task list
        datalist.innerHTML="";

        //render each task
     lists.forEach((list) => {
        if (list.namefield && list.incomefield ==="") {
            //alert open when u click submit and task is not entered
            alert('Please fill out all fields.');
            return;
        }

        //creating div to create table to manage the list to look unique and order 
        const div = document.createElement('div');
        div.classList="mydiv";
        datalist.appendChild(div);

        // Create a new table row
        const row = document.createElement('tr');

        // Create cells for name and income
        const nameCell = document.createElement('td');
        nameCell.textContent = list.name;

        const incomecell = document.createElement('td');
        incomecell.textContent = list.income;

        //create expense and savings btn
        const expense = document.createElement('td');
        const expensebtn = document.createElement('button');
        expensebtn.textContent = 'Add expenses';
        expensebtn.addEventListener("click", () => expenselist(list.id));
        expense.appendChild(expensebtn);

        const savings = document.createElement('td');
        const savingsbtn = document.createElement('button');
        savingsbtn.textContent = 'Add savings';
        savingsbtn.addEventListener("click", () => savingslist(list.id));
        savings.appendChild(savingsbtn);

        // Append cells to the row
        row.appendChild(nameCell);
        row.appendChild(incomecell);
        row.appendChild(expense);
        row.appendChild(savings);

        // Append the row to the table body
        tableBody.appendChild(row);

        //append the rows to the div
        div.appendChild(tableBody)

        // Clear input fields
        namefield.value = '';
        incomefield.value = '';

        
     });
    } catch (error) {
        console.error("Error fetching records",error);
        
    }
    
}

//add/update list
userform.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const id = useridfield.value;
    const name = namefield.value;
    const income = incomefield.value;

    if (!name || !income) {
        alert("Please enter valid data!");
        return;
    }
    const listdata = {name, income};

    try {
        if(id){
            //update list
            await fetch (`${API_URL}/details/${id}`,
                {
                    method: "PUT",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify(listdata),
                });
        } else {
            //create list
            await fetch(`${API_URL}/details`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(listdata),
                });
        }
        userform.reset();
        fetchdetails();
    } catch (error) {
        console.error("Error saving details:", error);
        alert("Failed to save the details. Please try again!")
    }
})

//////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////
//when i click add expenses
const expenselist = async () => {
    try {
        const response = await fetch(`${API_URL}/expenses`);
        if (!response.ok) {
            throw new Error(`HTTP error! status:${response.status}`);
            
        }
        const exlists = await response.json();
        //clear the current list
        exdatalist.innerHTML = "";


        const modal = document.getElementById('modal');
        const modalcontent = document.getElementById('modalcontent');
        const exform = document.getElementById('exform');
        const inputfield1 = document.getElementById('input1');
        const inputfield2 = document.getElementById('input2');
        const expensecontentfield = document.getElementById ('expensecontent');
        const exdatalist = document.getElementById('exdata');
        const extableBody = document.getElementById('expensetable');


        modal.style.display = 'block';

        //render each task
        exlists.forEach((exlist) => {
        if (exlist.inputfield1 && exlist.inputfield2 ==="") {
            //alert open when u click submit and task is not entered
            alert('Please fill out all fields.');
            return;
        }
 

        // Create a new table row
        const row1 = document.createElement('tr');

        // Create cells for name and income
        const expensecell = document.createElement('td');
        expensecell.textContent = exlist.input1;

        const amountcell = document.createElement('td');
        amountcell.textContent = exlist.input2;

        //create income remaining
        const remaining = document.createElement('td');
        const remainingValue = Number(list.income) - Number(amountcell);
        remaining.textContent = remainingValue;
        
        

        // Append cells to the row
        row1.appendChild(expensecell);
        row1.appendChild(amountcell);
        row1.appendChild(remaining);

        // Append the row to the table body
        extableBody.appendChild(row1);

        //append the rows to the div
        exdatalist.appendChild(extableBody)

        // Clear input fields
        inputfield1.value = '';
        inputfield2.value = '';

        
     });
     
        //close button functionality
        const closemodal = document.getElementById('closemodal');
        closemodal.onclick = function (event) {
            modal.style.display = 'none';

            expensecontentfield.style.display = 'block';

            //clear the current list
        exdatalist.innerHTML = "";
        }
        
        expensecontentfield.style.display = 'none';
      
    } catch (error) {
        
    }
}

//initial fetch
fetchdetails();
