from backend.server import app, db
from backend.server.models import Users, Department, Category, Asset, Request, RequestStatus, ReviewRequests
from datetime import datetime
from werkzeug.security import generate_password_hash  # To hash passwords

with app.app_context():
        print("Deleting data...")
        ReviewRequests.query.delete()
        Request.query.delete()
        RequestStatus.query.delete()
        Asset.query.delete()
        Category.query.delete()
        Department.query.delete()
        Users.query.delete()

        # Create Departments
        print("Creating departments...")
        hr_department = Department(department_name="Human Resources")
        it_department = Department(department_name="IT Department")
        finance_department = Department(department_name="Finance Department")
        marketing_department = Department(department_name="Marketing Department")
        sales_department = Department(department_name="Sales Department")
        operations_department = Department(department_name="Operations Department")
        support_department = Department(department_name="Support Department")
        legal_department = Department(department_name="Legal Department")
        r_and_d_department = Department(department_name="Research & Development")
        customer_success_department = Department(department_name="Customer Success Department")
        departments = [
            hr_department, it_department, finance_department, marketing_department, sales_department, operations_department, 
            support_department, legal_department, r_and_d_department, customer_success_department
        ]
        db.session.add_all(departments)

        # Create Categories
        print("Creating categories...")
        electronics_category = Category(category_name="Electronics", description="Electronic assets like laptops and phones.")
        furniture_category = Category(category_name="Furniture", description="Furniture assets like desks and chairs.")
        vehicles_category = Category(category_name="Vehicles", description="Company vehicles.")
        categories = [electronics_category, furniture_category, vehicles_category]
        db.session.add_all(categories)

        # Create Users
        print("Creating users...")
        user1 = Users(username="john_doe", email="john@example.com", password=generate_password_hash("password"), role="Admin", department=it_department)
        user2 = Users(username="jane_smith", email="jane@example.com", password=generate_password_hash("password"), role="Procurement Manager", department=finance_department)
        user3 = Users(username="alice_jones", email="alice@example.com", password=generate_password_hash("password"), role="Normal Member", department=hr_department)
        user4 = Users(username="bob_jones", email="bob@example.com", password=generate_password_hash("password"), role="Normal Member", department=marketing_department)
        user5 = Users(username="charlie_brown", email="charlie@example.com", password=generate_password_hash("password"), role="Normal Member", department=support_department)
        user6 = Users(username="david_lee", email="david@example.com", password=generate_password_hash("password"), role="Normal Member", department=operations_department)
        user7 = Users(username="eva_white", email="eva@example.com", password=generate_password_hash("password"), role="Admin", department=customer_success_department)
        user8 = Users(username="frank_garcia", email="frank@example.com", password=generate_password_hash("password"), role="Normal Member", department=legal_department)
        user9 = Users(username="grace_martin", email="grace@example.com", password=generate_password_hash("password"), role="Normal Member", department=r_and_d_department)
        user10 = Users(username="hank_clark", email="hank@example.com", password=generate_password_hash("password"), role="Normal Member", department=sales_department)
        users = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]
        db.session.add_all(users)
        db.session.commit()  # Commit to ensure users have IDs before proceeding

        # Create Assets
        print("Creating assets...")
        asset1 = Asset(asset_name="Laptop", description="MacBook Pro", category=electronics_category, department=it_department, allocated_to=1, status="In Use", image_url="http://bit.ly/48LzSRw")
        asset2 = Asset(asset_name="Office Chair", description="Ergonomic chair", category=furniture_category, department=hr_department, allocated_to=3, status="In Use", image_url="https://bit.ly/3O0G66D")
        asset3 = Asset(asset_name="Company Car", description="Toyota Corolla", category=vehicles_category, department=finance_department,status="Broken", image_url="https://bit.ly/4eo7ztB")
        asset4 = Asset(asset_name="Smartphone", description="iPhone 12", category=electronics_category, department=marketing_department, allocated_to=4, status="In Use", image_url="https://bit.ly/3UM8RYa")
        asset5 = Asset(asset_name="Projector", description="Epson Projector", category=furniture_category, department=support_department, allocated_to=5, status="Not In Use", image_url="https://bit.ly/4fJ8jKH")
        asset6 = Asset(asset_name="Printer", description="Canon Printer", category=furniture_category, department=operations_department,status="Broken", image_url="https://bit.ly/4fJ8VzZ")
        asset7 = Asset(asset_name="Desktop PC", description="HP Desktop", category=electronics_category, department=customer_success_department, allocated_to=7, status="In Use", image_url="https://bit.ly/4ejzsTy")
        asset8 = Asset(asset_name="Conference Phone", description="Cisco Phone", category=furniture_category, department=legal_department, allocated_to=8, status="In Use", image_url="https://bit.ly/4fxLrho")
        asset9 = Asset(asset_name="Smartwatch", description="Apple Watch", category=electronics_category, department=r_and_d_department, allocated_to=9, status="In Use", image_url="https://bit.ly/4eqVKTB")
        asset10 = Asset(asset_name="Desk Lamp", description="LED Desk Lamp", category=furniture_category, department=sales_department, allocated_to=10,status="In Use", image_url="https://bit.ly/3UPuTtd")
        asset11 = Asset(asset_name="Tablet", description="Samsung Galaxy Tab", category=electronics_category, department=it_department,allocated_to=9, status="In Use", image_url="https://tinyurl.com/4bj4kydz")
        asset12 = Asset(asset_name="Desk", description="Standing Desk", category=furniture_category, department=hr_department, allocated_to=3, status="In Use", image_url="https://tinyurl.com/3bkcdnkm")
        asset13 = Asset(asset_name="Monitor", description="Dell Monitor", category=electronics_category, department=marketing_department, allocated_to=4, status="In Use", image_url="https://tinyurl.com/hamp5sse")
        asset14 = Asset(asset_name="Keyboard", description="Wireless Keyboard", category=electronics_category, department=it_department, allocated_to=1, status="In Use", image_url="https://tinyurl.com/5n7kxj9s")
        asset15 = Asset(asset_name="Mouse", description="Logitech Mouse", category=electronics_category, department=it_department, allocated_to=1, status="In Use", image_url="https://tinyurl.com/mu69m9mu")
        asset16 = Asset(asset='H.O.D car', description='Toyota Camry', category=vehicles_category, department=it_department, allocated_to=1, status='In Use', image_url='https://tinyurl.com/yc8ev3vn')
        
        assets = [asset1, asset2, asset3, asset4, asset5, asset6, asset7, asset8, asset9, asset10, asset11, asset12, asset13, asset14, asset15, asset16]
        db.session.add_all(assets)

        # Create Request Statuses
        print("Creating request statuses...")
        status_pending = RequestStatus(status_name="Pending", description="Request is pending approval.")
        status_approved = RequestStatus(status_name="Approved", description="Request has been approved.")
        status_rejected = RequestStatus(status_name="Rejected", description="Request has been rejected.")
        statuses = [status_pending, status_approved, status_rejected]
        db.session.add_all(statuses)

        # Create Requests
        print("Creating requests...")
        request1 = Request(
            request_type="New Laptop",
            asset=asset1,
            requested_by=1, 
            department=it_department, 
            quantity=1,
            urgency="High",
            reason="Replacement needed",
            status=status_pending
        )

        request2 = Request(
            request_type="Office Chair",
            asset=asset2,
            requested_by=3,  
            department=hr_department, 
            quantity=1,
            urgency="Low",
            reason="Additional chair",
            status=status_approved
        )

        request3 = Request(
            request_type="Company Car",
            asset=asset3,
            requested_by=2,
            department=finance_department,
            quantity=1,
            urgency="Medium",
            reason="For business trips",
            status=status_pending
        )

        request4 = Request(
            request_type="Smartphone",
            asset=asset4,
            requested_by=4,
            department=marketing_department,
            quantity=1,
            urgency="High",
            reason="Work-related",
            status=status_approved
        )

        request5 = Request(
            request_type="Printer",
            asset=asset5,
            requested_by=5,
            department=support_department,
            quantity=1,
            urgency="Medium",
            reason="For office use",
            status=status_rejected
        )

        request6 = Request(
            request_type="Desktop PC",
            asset=asset7,
            requested_by=7,
            department=customer_success_department,
            quantity=1,
            urgency="High",
            reason="For new hire",
            status=status_approved
        )

        db.session.add_all([request1, request2, request3, request4, request5, request6])
        db.session.commit()  

        # Create Request Reviews
        print("Creating request reviews...")
        review1 = ReviewRequests(
            request=request1,  
            reviewed_by=2,  
            status=status_approved,
            review_comment="Approved for urgent need"
        )

        review2 = ReviewRequests(
            request=request2,  
            reviewed_by=1, 
            status=status_rejected,
            review_comment="Insufficient budget"
        )

        review3 = ReviewRequests(
            request=request3,  
            reviewed_by=3, 
            status=status_pending,
            review_comment="Under review"
        )

        review4 = ReviewRequests(
            request=request4,  
            reviewed_by=4, 
            status=status_approved,
            review_comment="Approved for urgent work"
        )

        review5 = ReviewRequests(
            request=request5,  
            reviewed_by=5, 
            status=status_rejected,
            review_comment="Rejected due to lack of resources"
        )

        review6 = ReviewRequests(
            request=request6,  
            reviewed_by=6, 
            status=status_approved,
            review_comment="Approved for new employee"
        )

        db.session.add_all([review1, review2, review3, review4, review5, review6])

        # Commit all changes
        db.session.commit()
        print("Seeding done!")

if __name__ == '__main__':
    app.run(debug=True)
