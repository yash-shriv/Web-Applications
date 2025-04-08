# Recipe Sharing Platform - Django Web Application

![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

A full-featured recipe sharing platform developed during my internship, enabling users to discover, create, and manage recipes with secure authentication.

## Project Overview
**Objective**: Create a collaborative space for food enthusiasts to share and discover recipes with robust access controls and search capabilities.

## Key Features Implemented

### 🍳 Recipe Management
- **Create/Edit/Delete** recipes with images, ingredients, and preparation steps
- **User-specific permissions** (CRUD operations limited to recipe owners)
- **Form security** with CSRF protection and input validation

### 🔍 Discovery Tools
- Keyword-based search using Django ORM (`icontains` queries)
- Frontend filtering for browsing recipes

### 🔐 User System
- Secure registration/login/logout flows
- Personalized dashboards showing user-owned recipes
- Django's built-in authentication extended for recipe ownership

## Technical Implementation Details

### Backend
- **14 functional endpoints** for core workflows
- **2 database models** (Recipe + User) with optimized relationships
- **MySQL database** with schema verified via MySQL Workbench
- **Django ORM** for efficient queries and case-insensitive search

### Security
- CSRF protection on all forms
- Input sanitization for user-generated content
- Session-based authentication

*Developed as part of my internship at TechnoHacks Solutions, contributing to the backend functionality while following enterprise development practices.*
