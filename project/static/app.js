// ----------------------
// TEACHERS
// ----------------------

function loadTeachers() {
    fetch("/teachers")
        .then(res => res.json())
        .then(data => {
            let table = document.querySelector("#teacherTable tbody");
            table.innerHTML = "";

            data.forEach(t => {
                table.innerHTML += `
                    <tr>
                        <td>${t.id}</td>
                        <td>${t.name}</td>
                        <td>${t.class_name}</td>
                        <td>
                            <button onclick="deleteTeacher(${t.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function addTeacher() {
    let teacher = {
        name: document.getElementById("tName").value,
        class_name: document.getElementById("tClass").value
    };

    fetch("/teachers", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(teacher)
    })
    .then(res => res.json())
    .then(() => loadTeachers());
}

function deleteTeacher(id) {
    fetch(`/teachers/${id}`, { method: "DELETE" })
        .then(() => loadTeachers());
}


let editingTeacherId = null;

function editTeacher(id, name, className) {
    editingTeacherId = id;
    document.getElementById("editTName").value = name;
    document.getElementById("editTClass").value = className;
}

function saveTeacher() {
    let teacher = {
        name: document.getElementById("editTName").value,
        class_name: document.getElementById("editTClass").value
    };

    fetch(`/teachers/${editingTeacherId}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(teacher)
    })
    .then(res => res.json())
    .then(() => loadTeachers());
}




// ----------------------
// STUDENTS
// ----------------------

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
                        <td>${s.class_name}</td>
                        <td>${s.teacher_id}</td>
                        <td>${s.qualification_level}</td>
                        <td>
                            <button onclick="deleteStudent(${s.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function addStudent() {
    let student = {
        name: document.getElementById("sName").value,
        class_name: document.getElementById("sClass").value,
        teacher_id: parseInt(document.getElementById("sTeacher").value),
        qualification_level: document.getElementById("sQual").value
    };

    fetch("/students", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(student)
    })
    .then(res => res.json())
    .then(() => loadStudents());
}

function deleteStudent(id) {
    fetch(`/students/${id}`, { method: "DELETE" })
        .then(() => loadStudents());
}


let editingStudentId = null;

function editStudent(id, name, className, teacherId, qual) {
    editingStudentId = id;
    document.getElementById("editSName").value = name;
    document.getElementById("editSClass").value = className;
    document.getElementById("editSTeacher").value = teacherId;
    document.getElementById("editSQual").value = qual;
}

function saveStudent() {
    let student = {
        name: document.getElementById("editSName").value,
        class_name: document.getElementById("editSClass").value,
        teacher_id: parseInt(document.getElementById("editSTeacher").value),
        qualification_level: document.getElementById("editSQual").value
    };

    fetch(`/students/${editingStudentId}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(student)
    })
    .then(res => res.json())
    .then(() => loadStudents());
}
