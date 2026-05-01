let editingId = null;

// LOAD
function loadStudents() {
    fetch("/students")
        .then(res => res.json())
        .then(data => {
            let table = document.querySelector("#studentTable tbody");
            table.innerHTML = "";

            data.forEach(s => {
                table.innerHTML += `
                    <tr>
                        <td>${s.id}</td>
                        <td>${s.name}</td>
                        <td>${s.address}</td>
                        <td>${s.email}</td>
                        <td>${s.course}</td>
                        <td>
                            <button onclick="editStudent(${s.id}, '${s.name}', '${s.address}', '${s.email}', '${s.course}')">Edit</button>
                            <button onclick="deleteStudent(${s.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

// CREATE
function addStudent() {
    let student = {
        name: document.getElementById("name").value,
        address: document.getElementById("address").value,
        email: document.getElementById("email").value,
        course: document.getElementById("course").value
    };

    fetch("/students", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(student)
    }).then(() => loadStudents());
}

// DELETE
function deleteStudent(id) {
    fetch(`/students/${id}`, { method: "DELETE" })
        .then(() => loadStudents());
}

// EDIT (load into form)
function editStudent(id, name, address, email, course) {
    editingId = id;
    document.getElementById("editName").value = name;
    document.getElementById("editAddress").value = address;
    document.getElementById("editEmail").value = email;
    document.getElementById("editCourse").value = course;
}

// UPDATE
function saveStudent() {
    let student = {
        name: document.getElementById("editName").value,
        address: document.getElementById("editAddress").value,
        email: document.getElementById("editEmail").value,
        course: document.getElementById("editCourse").value
    };

    fetch(`/students/${editingId}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(student)
    }).then(() => loadStudents());
}
