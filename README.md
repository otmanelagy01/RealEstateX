# RealEstateX Module Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Module Structure](#module-structure)
4. [Functionality](#functionality)
   - [Complaint Form](#complaint-form)
   - [Back-office Pipeline](#back-office-pipeline)
   - [Work Order Generation](#work-order-generation)
5. [Usage](#usage)
   - [Accessing the Complaint Form](#accessing-the-complaint-form)
   - [Managing Complaints in the Back-office](#managing-complaints-in-the-back-office)
   - [Generating Work Orders](#generating-work-orders)
6. [Conclusion](#conclusion)

## 1. Introduction<a name="introduction"></a>

The RealEstateX module is designed to streamline the complaint management process for a company. It provides a web-based complaint form for tenants to submit their complaints and a back-office pipeline for employees to manage and respond to these complaints. The module also includes functionality to generate work orders for complaints that require intervention.

## 2. Installation<a name="installation"></a>

To install the RealEstateX module, follow these steps:

1. Download the module files.
2. Place the module directory in the Odoo `addons` directory.
3. Restart the Odoo server.
4. Install the module from the Odoo Apps menu in the Odoo backend.

## 3. Module Structure<a name="module-structure"></a>

The RealEstateX module consists of the following main components:

- `models/realestatex_complaint.py`: Defines the `Realestatex Complaint` model, which represents a complaint submitted by a tenant.
- `views/realestatex_complaint_views.xml`: Contains the XML views for the `RealestatexComplaint` model, including the complaint form and back-office views.
- `reports/work_order_report.xml`: Contains the qweb template for the work order report.
- `data/sequence.xml`: Contains the sequence definition for generating complaint numbers.
- `security/ir.model.access.csv`: Defines the access rights for the `RealestatexComplaint` model.

## 4. Functionality<a name="functionality"></a>

### Complaint Form<a name="complaint-form"></a>

The module provides a web-based complaint form that allows tenants to submit their complaints. The form includes fields for identifying the tenant (name, email) and the rented flat (address), as well as fields to describe the problem (complaint type, description).

### Back-office Pipeline<a name="back-office-pipeline"></a>

In the backend, employees can view and manage the complaints submitted by tenants. Complaints are automatically assigned to a customer service representative, who can classify the complaint and decide on an action plan. The pipeline includes stages for new complaints, complaints in review, complaints in progress, solved complaints, and dropped complaints.

### Work Order Generation<a name="work-order-generation"></a>

For complaints that require intervention, a customer service supervisor can generate a work order containing details of the complaint (customer, address, date, action plan, etc.). The work order follows the DIN 5008 standard for business documents.

## 5. Usage<a name="usage"></a>

### Accessing the Complaint Form<a name="accessing-the-complaint-form"></a>

Tenants can access the complaint form from the RealEstateX website. The form is available without authentication, allowing tenants to submit complaints easily.

### Managing Complaints in the Back-office<a name="managing-complaints-in-the-back-office"></a>

Employees can access the back-office pipeline from the Odoo backend. They can view and manage complaints, assign complaints to customer service representatives, and track the progress of complaints through the different stages.

### Generating Work Orders<a name="generating-work-orders"></a>

To generate a work order for a complaint, a customer service supervisor can select the complaint in the backend and use the "Generate Work Order" button. The work order will be generated following the DIN 5008 standard and can be printed or saved as a PDF.

## 6. Conclusion<a name="conclusion"></a>

The RealEstateX module provides an efficient solution for managing tenant complaints. By providing a web-based complaint form and a back-office pipeline, the module helps streamline the complaint management process and improve tenant satisfaction.
