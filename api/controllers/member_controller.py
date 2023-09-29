from flask import request, jsonify
from ..models.member_model import Member


class MemberController:
    """Member controller class"""

    @classmethod
    def create(cls):
        """Create a new member"""
        data = request.json
        member = Member(user_id=data.get('user_id'), server_id=data.get('server_id'))

        Member.create(member)
        return {'message': 'Member created successfully'}, 201

    @classmethod
    def get_all(cls):
        """Get all members"""
        member_objects = Member.get_all()
        members = []
        for member in member_objects:
            members.append(member.serialize())
        return members, 200

    @classmethod
    def get(cls, member_id):
        """Get member details by ID"""
        member = Member(member_id=member_id)

        result = Member.get(member)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def delete(cls, member_id):
        """Delete a member by ID"""
        member = Member(member_id=member_id)

        Member.delete(member)
        return {'message': 'Member deleted successfully'}, 200

    @classmethod
    def serialize(cls, member):
        return {
            'id': member.id,
            'user_id': member.user_id,
            'server_id': member.server_id,         
        }
    
    @classmethod
    def get_member_user(cls, user_id):
        """Get member details by ID"""
        """Get all members"""
        member_objects = Member.get_member_user(user_id)
        members = []
        for member in member_objects:
            members.append(member.serialize())
        return members, 200
