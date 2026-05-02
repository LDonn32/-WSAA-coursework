let editingId = null;

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
                            <button onclick="editStudent(${s.id}, '${escapeJs(s.name)}', '${escapeJs(s.address)}', '${escapeJs(s.email)}', '${escapeJs(s.course)}')">Edit</button>
                            <button onclick="deleteStudent(${s.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

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
    }).then(() => {
        clearAddForm();
        loadStudents();
    });
}

function deleteStudent(id) {
    fetch(`/students/${id}`, { method: "DELETE" })
        .then(() => loadStudents());
}

function editStudent(id, name, address, email, course) {
    editingId = id;
    document.getElementById("editName").value = name;
    document.getElementById("editAddress").value = address;
    document.getElementById("editEmail").value = email;
    document.getElementById("editCourse").value = course;
}

function saveStudent() {
    if (!editingId) return alert("Select a student to edit first.");
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
    }).then(() => {
        editingId = null;
        clearEditForm();
        loadStudents();
    });
}

function clearAddForm() {
    document.getElementById("name").value = "";
    document.getElementById("address").value = "";
    document.getElementById("email").value = "";
    document.getElementById("course").value = "";
}

function clearEditForm() {
    document.getElementById("editName").value = "";
    document.getElementById("editAddress").value = "";
    document.getElementById("editEmail").value = "";
    document.getElementById("editCourse").value = "";
}

/* small helper to escape single quotes when injecting into onclick strings */
function escapeJs(s) {
    if (!s) return '';
    return s.replace(/'/g, "\\'");
}
