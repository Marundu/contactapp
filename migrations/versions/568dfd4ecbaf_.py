"""empty message

Revision ID: 568dfd4ecbaf
Revises: 
Create Date: 2018-10-10 21:11:40.997167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '568dfd4ecbaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contactdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('email', sa.String(length=140), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('feedback', sa.String(length=250), nullable=True),
    sa.Column('date_sent', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contactdetails_email'), 'contactdetails', ['email'], unique=False)
    op.create_index(op.f('ix_contactdetails_name'), 'contactdetails', ['name'], unique=False)
    op.create_index(op.f('ix_contactdetails_phone_number'), 'contactdetails', ['phone_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contactdetails_phone_number'), table_name='contactdetails')
    op.drop_index(op.f('ix_contactdetails_name'), table_name='contactdetails')
    op.drop_index(op.f('ix_contactdetails_email'), table_name='contactdetails')
    op.drop_table('contactdetails')
    # ### end Alembic commands ###
